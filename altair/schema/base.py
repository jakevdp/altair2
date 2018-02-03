import jsonschema
import inspect

Undefined = object()


class BaseObject(object):
    _json_schema = {}
    _attr_names_to_ignore = ['_attr_names_to_ignore', '_json_schema']

    def __init__(self, **kwds):
        for key, val in kwds.items():
            setattr(self, key, val)

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
        dct = {attr: val.to_dict(validate=validate)
               if isinstance(val, BaseObject) else val
               for attr, val in self.__attr_dict().items()
               if val is not Undefined}
        if validate:
            jsonschema.validate(dct, self._json_schema)
        return dct
