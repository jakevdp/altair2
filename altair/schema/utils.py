"""Utilities for working with schemas"""

import keyword
import json
import re


EXCLUDE_KEYS = ('definitions', 'title', 'description', '$schema', 'id')


def hash_schema(schema, use_json=True, exclude_keys=EXCLUDE_KEYS):
    """
    Compute a python hash for a nested dictionary which
    properly handles dicts, lists, sets, and tuples.

    At the top level, the function excludes from the hashed schema all keys
    listed in `exclude_keys`.

    This implements two methods: one based on conversion to JSON, and one based
    on recursive conversions of unhashable to hashable types; the former seems
    to be slightly faster in several benchmarks.
    """
    if exclude_keys:
        schema = {key: val for key, val in schema.items()
                  if key not in exclude_keys}
    if use_json:
        s = json.dumps(schema, sort_keys=True)
        return hash(s)
    else:
        def _freeze(val):
            if isinstance(val, dict):
                return frozenset((k, _freeze(v)) for k, v in val.items())
            elif isinstance(val, set):
                return frozenset(map(_freeze, val))
            elif isinstance(val, list) or isinstance(val, tuple):
                return tuple(map(_freeze, val))
            else:
                return val
        return hash(_freeze(schema))


def resolve_references(schema, context=None):
    """Resolve References within a JSON schema"""
    if context is None:
        context = schema
    if '$ref' in schema:
        address = schema['$ref'].split('/')
        assert address[0] == '#'
        schema = context
        for key in address[1:]:
            schema = schema[key]
        return resolve_references(schema, context)
    else:
        return schema


def get_valid_identifier(prop, replacement_character='', allow_unicode=False):
    """Given a string property, generate a valid Python identifier"""
    # First substitute-out all non-valid characters.
    flags = re.UNICODE if allow_unicode else re.ASCII
    valid = re.sub('\W', replacement_character, prop, flags=flags)

    # If nothing is left, use just an underscore
    if not valid:
        valid = '_'

    # first character must be a non-digit. Prefix with an underscore
    # if needed
    if re.match('^[\d\W]', valid):
        valid = '_' + valid

    # if the result is a reserved keyword, then add an underscore at the end
    if keyword.iskeyword(valid):
        valid += '_'
    return valid


class SchemaInfo(object):
    _defaults = {'properties': {},
                 'required': [],
                 'patternProperties': {},
                 'additionalProperties': True,
                 'type': None}
    def __init__(self, schema):
        self.raw_schema = schema
        self.schema = resolve_references(schema)
        for key, default in self._defaults.items():
            setattr(self, key, self.schema.get(key, default))

    def is_empty(self):
        return set(self.schema.keys()) - set(EXCLUDE_KEYS) == {}

    def is_compound(self):
        return any(key in self.schema for key in ['anyOf', 'allOf', 'oneOf'])

    def is_object(self):
        if self.type == 'object':
            return True
        elif self.type is not None:
            return False
        elif self.properties or self.required or self.patternProperties or self.additionalProperties:
            return True
        else:
            raise ValueError("Unclear whether schema.is_object() is True")

    def is_value(self):
        return not self.is_object()

    def property_name_map(self):
        """
        Return a mapping of schema property names to valid Python attribute names

        Only properties which are not valid Python identifiers will be included in
        the dictionary.
        """
        pairs = [(prop, get_valid_identifier(prop)) for prop in self.properties]
        return {prop: val for prop, val in pairs if prop != val}

    def init_code(self, classname):
        """Return code suitable for the __init__ function of a Schema class"""

        if self.is_empty() or self.is_compound():
            args = ['*args', '**kwds']
            super_args = ['*args', '**kwds']
        elif self.is_value():
            args = ['*args']
            super_args = ['*args']
        else:
            map_ = self.property_name_map()
            required = {map_.get(p, p) for p in self.required}
            properties = {map_.get(p, p) for p in self.properties} - required
            extra_args = (self.additionalProperties != False)

            args = sorted(required) + ['{0}=Undefined'.format(prop)
                                       for prop in sorted(properties)]
            super_args = ['{0}={0}'.format(prop)
                          for prop in (sorted(required) + sorted(properties))]
            if extra_args:
                args.append('**kwds')
                super_args.append('**kwds')

        signature = ("def __init__({args}):\n"
                     "    super({classname}, self).__init__({super_args})")
        return signature.format(classname=classname,
                                args=', '.join(['self'] + args),
                                super_args=', '.join(super_args))

    def docstring(self, classname):
        # TODO: more useful doc string
        return '"""A {classname} json schema wrapper"""'.format(classname=classname)