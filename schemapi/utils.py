"""Utilities for working with schemas"""

import keyword
import json
import re
import textwrap


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
        # Add definitions
        if 'definitions' in context and 'definitions' not in schema:
            return dict(definitions=context['definitions'], **schema)
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


def is_valid_identifier(var, allow_unicode=False):
    """Return true if var contains a valid Python identifier

    Parameters
    ----------
    val : string
        identifier to check
    allow_unicode : bool (default: False)
        if True, then allow Python 3 style unicode identifiers.
    """
    flags = re.UNICODE if allow_unicode else re.ASCII
    is_valid = re.match("^[^\d\W]\w*\Z", var, flags)
    return is_valid and not keyword.iskeyword(var)


def indent_function_args(funcname, arglist, indent=0, width=100):
    initial_indent = subsequent_indent = (len(funcname) + indent + 1) * ' '
    wrapper = textwrap.TextWrapper(width=width,
                                   initial_indent=initial_indent,
                                   subsequent_indent=subsequent_indent,
                                   break_long_words=False)
    return '{0}({1})'.format(funcname,
                             '\n'.join(wrapper.wrap(', '.join(arglist))))



def indent_line(line, initial_indent=0, width=120, initial_width=120,
                subsequent_indent=4):
    wrapper = textwrap.TextWrapper(width=width,
                                   initial_indent=(width - initial_width)* ' ',
                                   subsequent_indent=subsequent_indent * ' ',
                                   break_long_words=False)
    return '\n'.join(wrapper.wrap(line)).lstrip()


class SchemaProperties(object):
    def __init__(self, properties, schema):
        self.__properties = properties
        self.__schema = schema

    def __dir__(self):
        return list(self.__properties.keys())

    def __getattr__(self, attr):
        return self[attr]

    def __getitem__(self, attr):
        dct = self.__properties[attr]
        if 'definitions' in self.__schema and 'definitions' not in dct:
            dct = dict(definitions=self.__schema['definitions'], **dct)
        return SchemaInfo(dct)

    def __iter__(self):
        return iter(self.__properties)

    def items(self):
        return self.__properties.items()

    def keys(self):
        return self.__properties.keys()

    def values():
        return self.__properties.values()


class SchemaInfo(object):
    def __init__(self, schema):
        if not isinstance(schema, dict):
            schemaname = "_{0}__schema".format(schema.__name__)
            schema = getattr(schema, schemaname)
        self.raw_schema = schema
        self.schema = resolve_references(self.raw_schema)

    def __repr__(self):
        keys = []
        for key in sorted(self.schema.keys()):
            val = self.schema[key]
            rval = repr(val).replace('\n', '')
            if len(rval) > 30:
                rval = rval[:30] + '...'
            if key == 'definitions':
                rval = "{...}"
            elif key == 'properties':
                rval = '{\n    ' + '\n    '.join(sorted(map(repr, val))) + '\n  }'
            keys.append('"{0}": {1}'.format(key, rval))
        return "SchemaInfo({\n  " + '\n  '.join(keys) + "\n})"

    @property
    def properties(self):
        return SchemaProperties(self.schema.get('properties', {}), self.schema)

    @property
    def definitions(self):
        return SchemaProperties(self.schema.get('definitions', {}), self.schema)

    @property
    def required(self):
        return self.schema.get('required', [])

    @property
    def patternProperties(self):
        return self.schema.get('patternProperties', {})

    @property
    def additionalProperties(self):
        return self.schema.get('additionalProperties', True)

    @property
    def type(self):
        return self.schema.get('type', None)

    @property
    def anyOf(self):
        return self.schema.get('anyOf', [])

    @property
    def oneOf(self):
        return self.schema.get('oneOf', [])

    @property
    def allOf(self):
        return self.schema.get('allOf', [])

    @property
    def items(self):
        return self.schema.get('items', {})

    @property
    def enum(self):
        return self.schema.get('enum', [])

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

    def is_array(self):
        return (self.type == 'array')

    def schema_type(self):
        if self.is_empty():
            return 'empty'
        elif self.is_compound():
            for key in ['anyOf', 'oneOf', 'allOf']:
                if key in self.schema:
                    return key
        elif self.is_object():
            return 'object'
        elif self.is_array():
            return 'array'
        elif self.is_value():
            return 'value'
        else:
            raise ValueError("Unknown type with keys {0}".format(self.schema))

    def property_name_map(self):
        """
        Return a mapping of schema property names to valid Python attribute names

        Only properties which are not valid Python identifiers will be included in
        the dictionary.
        """
        pairs = [(prop, get_valid_identifier(prop)) for prop in self.properties]
        return {prop: val for prop, val in pairs if prop != val}


    def init_code(self, classname, indent=4):
        """Return code suitable for the __init__ function of a Schema class"""

        args = ['self']

        if self.is_empty() or self.is_compound():
            args += ['*args', '**kwds']
            super_args = ['*args', '**kwds']
            invalid_props = None
            invalid_required_props = None
        elif self.is_value():
            args += ['*args']
            super_args = ['*args']
            invalid_props = None
            invalid_required_props = None
        else:
            all_props = set(self.properties)
            valid_props = {p for p in all_props if is_valid_identifier(p)}
            invalid_props = all_props - valid_props
            required_props = set(self.required)
            valid_required_props = required_props - invalid_props
            invalid_required_props = required_props - valid_required_props
            valid_nonrequired_props = valid_props - required_props
            extra_args = (self.additionalProperties != False)

            args += sorted(valid_required_props)
            args += ['{0}=Undefined'.format(prop) for prop in sorted(valid_nonrequired_props)]
            super_args = ['{0}={0}'.format(prop)
                          for prop in (sorted(valid_required_props) + sorted(valid_nonrequired_props))]
            if extra_args or invalid_props:
                args.append('**kwds')
                super_args.append('**kwds')

        code = ["def __init__({0}):".format(', '.join(args))]
        if invalid_required_props:
            code.append("# make certain required properties with invalid identifiers are in kwds")
            code.append("missing_kwds = {0} - set(kwds)".format(repr(invalid_required_props)))
            code.append("if missing_kwds:")
            code.append("    raise TypeError('missing required keyword arguments: {0}'.format(missing_kwds))")
            code.append("")
        if invalid_props and not extra_args:
            code.append("# additionalProperties=False, so make sure kwds only contains recognized properties")
            code.append("unrecognized_kwds = set(kwds) - {0}".format(repr(invalid_props)))
            code.append("if unrecognized_kwds:")
            code.append("    raise TypeError('unexpected keyword arguments {0}').format(unrecognized_kwds)")
            code.append("")
        code.append("super({0}, self).__init__({1})".format(classname, ', '.join(super_args)))

        print(('\n' + indent * ' ').join(code))

        # TODO: wrap arguments at 80 chars
        return ('\n' + indent * ' ').join(code)

    def docstring(self, classname, repr=True):
        # TODO: more useful doc string
        doc = '"""A {classname} json schema wrapper"""'.format(classname=classname)
        if repr:
            return doc
        else:
            return eval(doc)
