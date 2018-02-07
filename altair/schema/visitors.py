from collections import defaultdict

import jsonschema

from .utils import SchemaInfo, resolve_references, hash_schema


class FromDict(object):
    def __init__(self, class_list):
        self.class_dict = defaultdict(list)
        for cls in class_list:
            self.class_dict[cls._json_schema_hash()].append(cls)

    def from_dict(self, schemacls, dct, validate=True):
        # TODO: implement additionalProperties & patternProperties
        if validate:
            jsonschema.validate(dct, schemacls._json_schema)

        schema = resolve_references(schemacls._json_schema)

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
        schema = resolve_references(schemacls._json_schema)
        schemas = schema.get('anyOf', []) + schema.get('oneOf', [])
        for schema in schemas:
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
        schema = resolve_references(schemacls._json_schema)
        map_ = schemacls._valid_attr_map
        props = schema.get('properties', {})
        hashes = {prop: hash_schema(val) for prop, val in props.items()}
        matches = {prop: self.class_dict[hash_]
                   for prop, hash_ in hashes.items()}
        # TODO: do something more than simply selecting the last match?
        wrappers = {prop: match[-1] for prop, match in matches.items() if match}
        kwds = {map_.get(key, key): (wrappers[key].from_dict(val, validate=validate)
                                     if key in wrappers else val)
                for key, val in dct.items()}
        return schemacls(**kwds)

    def _from_dict_list(self, schemacls, dct, validate=False):
        # TODO: find wrapper class for elements in items
        return schemacls(dct)
