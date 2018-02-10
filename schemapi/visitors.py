from collections import defaultdict

import jsonschema

from .utils import SchemaInfo, resolve_references, hash_schema


class FromDict(object):
    def __init__(self, class_list):
        self.class_dict = defaultdict(list)
        for cls in class_list:
            self.class_dict[hash_schema(self._get_schema(cls))].append(cls)

    def _get_schema(self, cls, resolve_refs=False):
        # "private" variable name mangling
        schema = getattr(cls, '_{0}__schema'.format(cls.__name__), {})
        if resolve_refs:
            schema = resolve_references(schema)
        return schema

    def from_dict(self, schemacls, dct, validate=True):
        # TODO: implement additionalProperties & patternProperties
        if validate:
            jsonschema.validate(dct, self._get_schema(schemacls))

        schema = self._get_schema(schemacls, resolve_refs=True)

        if 'anyOf' in schema or 'oneOf' in schema:
            obj = self._from_dict_union(schemacls, dct)
            if obj is not None:
                return obj

        if isinstance(dct, dict):
            return self._from_dict_object(schemacls, dct)
        elif isinstance(dct, list):
            return self._from_dict_list(schemacls, dct)
        else:
            return schemacls(dct)

    def _from_dict_union(self, schemacls, dct):
        schema = self._get_schema(schemacls, resolve_refs=True)
        schemas = schema.get('anyOf', []) + schema.get('oneOf', [])
        for schema in schemas:
            # TODO: in the no-match case, call from_dict on dict/list contents
            matches = self.class_dict[hash_schema(schema)]
            if not matches:
                continue
            try:
                obj = matches[-1].from_dict(dct, validate=True)
            except TypeError:
                continue
            except jsonschema.ValidationError:
                continue
            else:
                return obj
        return None

    def _from_dict_object(self, schemacls, dct, validate=False):
        schema = self._get_schema(schemacls, resolve_refs=True)
        props = schema.get('properties', {})
        hashes = {prop: hash_schema(val) for prop, val in props.items()}
        matches = {prop: self.class_dict[hash_]
                   for prop, hash_ in hashes.items()
                   if hash_ in self.class_dict}
        # TODO: do something more than simply selecting the last match?
        wrappers = {prop: match[-1] for prop, match in matches.items()}
        kwds = {key: (wrappers[key].from_dict(val, validate=validate)
                      if key in wrappers else val)
                for key, val in dct.items()}
        return schemacls(**kwds)

    def _from_dict_list(self, schemacls, dct, validate=False):
        # TODO: find wrapper class for elements in items
        return schemacls(dct)
