import jsonschema
import inspect

Undefined = object()


def hash_schema(val):
    """
    Compute a unique hash of a nested dictionary, properly handling dicts,
    lists, and sets.
    """
    def _freeze(val):
        if isinstance(val, dict):
            return frozenset((k, _freeze(v)) for k, v in val.items())
        elif isinstance(val, set):
            return frozenset(map(_freeze, val))
        elif isinstance(val, list) or isinstance(val, tuple):
            return tuple(map(_freeze, val))
        else:
            return val
    return hash(_freeze(val))


class BaseObject(object):
    _json_schema = {}
    _attr_names_to_ignore = ('_attr_names_to_ignore', '_json_schema')

    def __init__(self, **kwds):
        for key, val in kwds.items():
            setattr(self, key, val)

    @classmethod
    def _json_schema_hash(cls):
        """Return a unique hash of this class' _json_schema"""
        return hash_schema(cls._json_schema)

    def __attrs(self):
        """Return a list of instance attributes"""
        members = inspect.getmembers(self, lambda a: (not inspect.isroutine(a)))
        return [name for name, val in members
                if not (name.startswith('__') and name.endswith('__'))
                and name not in self._attr_names_to_ignore]

    def __attr_dict(self):
        """return a dicitionary of attributes to values"""
        return {attr: getattr(self, attr) for attr in self.__attrs()}

    def to_dict(self, validate=True):
        """return a dictionary representation of the object"""
        dct = {attr: (val.to_dict(validate=validate)
                      if isinstance(val, BaseObject) else val)
               for attr, val in self.__attr_dict().items()
               if val is not Undefined}
        if validate:
            jsonschema.validate(dct, self._json_schema)
        return dct
