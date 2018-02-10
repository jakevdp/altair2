import collections
import inspect
import json
import keyword
import re
import warnings

import jsonschema

from .utils import hash_schema, SchemaInfo, resolve_references
from . import codegen


class UndefinedType(object):
    """A singleton object for marking undefined attributes"""
    __instance = None
    def __new__(cls, *args, **kwargs):
        if not isinstance(cls.__instance, cls):
            cls.__instance = object.__new__(cls, *args, **kwargs)
        return cls.__instance
    def __repr__(self):
        return 'Undefined'
Undefined = UndefinedType()


def schemaclass(*args, init_func=True, docstring=True, property_map=True):
    """A decorator to add boilerplate to a schema class

    This will read the _json_schema attribute of a SchemaBase class, and add
    one or all of three attributes/methods, based on the schema:

    - An __init__ function
    - a __doc__ docstring

    In all cases, if the attribute/method is explicitly defined in the class
    it will not be overwritten.

    A simple invocation adds all three attributes/methods:

        @schemaclass
        class MySchema(SchemaBase):
            __schema = {...}

    Optionally, you can invoke schemaclass with arguments to turn off
    some of the added behaviors:

        @schemaclass(init_func=True, docstring=False)
        class MySchema(SchemaBase):
            __schema = {...}
    """
    def _decorator(cls, init_func=init_func, docstring=docstring):
        if not isinstance(cls, SchemaBase):
            warnings.warn("class is not an instance of SchemaBase.")

        name = cls.__name__
        schema_name = '_{0}__schema'.format(name)
        schema = SchemaInfo(getattr(cls, schema_name, {}))

        if init_func and '__init__' not in cls.__dict__:
            init_code = codegen.init_code(name, schema.schema)
            globals_ = {name: cls, 'Undefined': Undefined}
            locals_ = {}
            exec(init_code, globals_, locals_)
            setattr(cls, '__init__', locals_['__init__'])

        if docstring and not cls.__doc__:
            setattr(cls, '__doc__', codegen.docstring(name, schema.schema))
        return cls

    if len(args) == 0:
        return _decorator
    elif len(args) == 1:
        return _decorator(args[0])
    else:
        raise ValueError("optional arguments to schemaclass must be "
                         "passed by keyword")


class SchemaBase(object):
    """Base class for schema wrappers.

    Each derived class should set the _json_schema class attribute which is
    used for validation. If not specified in the class definition, an
    appropriate __init__ function will be generated by SchemaBaseMeta.
    """
    __schema = {}

    def __init__(self, *args, **kwds):
        # Two valid options for initialization, which should be handled by
        # derived classes:
        # - a single arg with no kwds, for, e.g. {'type': 'string'}
        # - zero args with zero or more kwds for {'type': 'object'}
        assert len(args) == (0 if kwds else 1)
        self.__args = args
        self.__kwds = kwds

    def __getattr__(self, item):
        # reminder: getattr is called after the normal lookups
        return self.__kwds[item]

    def __setattr__(self, item , val):
        if item in ['_SchemaBase__args', '_SchemaBase__kwds']:
            object.__setattr__(self, item, val)
        else:
            self.__kwds[item] = val

    def __getitem__(self, item):
        return self.__kwds[item]

    def __setitem__(self, item, val):
        self.__kwds[item] = val

    def __repr__(self):
        val = self.__args
        dct = self.__kwds
        if dct:
            args = ("{0!r}: {1!r}".format(key, val)
                    for key, val in dct.items()
                    if val is not Undefined)
            args = '\n' + ',\n'.join(args)
            args = args.replace('\n', '\n  ')
            return "{0}(**{{{1}\n}})".format(self.__class__.__name__, args)
        else:
            return "{0}({1})".format(self.__class__.__name__, val[0])

    def __get_schema(self):
        """
        Return the schema defined in this class, if it exists, or an empty dict.
        """
        return getattr(self, '_{0}__schema'.format(self.__class__.__name__), {})

    def to_dict(self, validate=True, **kwds):
        """Return a dictionary representation of the object

        Parameters
        ----------
        validate : boolean
            If True (default), then validate the output dictionary
            against the schema.

        Returns
        -------
        dct : dictionary
            The dictionary representation of this object

        Raises
        ------
        jsonschema.ValidationError :
            if validate=True and the dict does not conform to the schema
        """
        def _todict(val):
            if isinstance(val, SchemaBase):
                # only validate at the top level
                return val.to_dict(validate=False)
            elif isinstance(val, list):
                return [_todict(v) for v in val]
            elif isinstance(val, dict):
                return {k: _todict(v) for k, v in val.items()}
            else:
                return val

        dct = {attr: _todict(v)
               for attr, v in self.__kwds.items()
               if v is not Undefined and kwds.get(attr, True)}
        val = self.__args

        if val and len(dct) > 0:
            raise ValueError("{0} instance has both a value and properties : "
                             "cannot serialize to dict")

        if val:
            result = _todict(val[0])
        else:
            result = _todict(dct)

        if validate:
            jsonschema.validate(result, self.__get_schema())
        return result

    @classmethod
    def from_dict(cls, dct, validate=True):
        """Construct class from a dictionary representation

        Parameters
        ----------
        dct : dictionary
            The dict from which to construct the class
        validate : boolean
            If True (default), then validate the output dictionary
            against the schema.

        Returns
        -------
        obj : Schema object
            The wrapped schema

        Raises
        ------
        jsonschema.ValidationError :
            if validate=True and dct does not conform to the schema
        """
        converter = FromDict(SchemaBase.__subclasses__())
        return converter.from_dict(cls, dct, validate=validate)


class FromDict(object):
    def __init__(self, class_list):
        self.class_dict = collections.defaultdict(list)
        for cls in class_list:
            self.class_dict[hash_schema(self._get_schema(cls))].append(cls)

    def _get_schema(self, cls, resolve_refs=False):
        # "private" variable name mangling
        schema = getattr(cls, '_{0}__schema'.format(cls.__name__), {})
        if resolve_refs:
            schema = resolve_references(schema)
        return schema

    def from_dict(self, schemacls, dct, validate=True):
        # TODO: change this to take schema rather than schemacls & use below
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
                # TODO: call self.from_dict instead
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
        schema = self._get_schema(schemacls, resolve_refs=True)
        if 'items' in schema:
            hash_ = hash_schema(schema['items'])
            wrapper = self.class_dict[hash_]
        else:
            wrapper = []

        if wrapper:
            return schemacls([wrapper[-1].from_dict(val) for val in dct])
        else:
            return schemacls(dct)
