import collections
import inspect
import json

import jsonschema
import six


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


def resolve_references(schema, context=None):
    """Resolve References"""
    if context is None:
        context = schema
    if '$ref' in schema:
        address = schema['$ref'].split('/')
        assert address[0] == '#'
        schema = context
        print(schema)
        for key in address[1:]:
            schema = schema[key]
        return resolve_references(schema, context)
    else:
        return schema


def hash_schema(schema, use_json=True,
                exclude_keys=['definitions', 'description', '$schema']):
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


def init_code(schema, classname):
    """Given a JSON schema, create an appropriate __init__ function"""
    schema = resolve_references(schema)

    # find required properties
    required = set(schema.get('required', []))

    # find listed properties
    props = set(schema.get('properties', [])) - required

    # find whether additional properties are allowed
    additional_props = schema.get('additionalProperties', {})
    pattern_props = schema.get('patternProperties', {})
    allow_extra_kwds = pattern_props or additional_props or (additional_props == {})

    # determine whether this is an object, a value, or perhaps both
    type_ = schema.get('type', None)
    is_object = type_ in ['object', None]
    is_value = (not is_object) or (type_ is None and not (props or required))

    # build function signature
    args = ['self']
    if is_value:
        # TODO: prevent name collisions
        args.append('value_')
    if is_object:
        args.extend(sorted(required))
        args.extend(sorted(['{0}=Undefined'.format(prop) for prop in props]))
        if allow_extra_kwds:
            args.append('**kwds')
    signature = "def __init__({0}):".format(', '.join(args))

    # function contents
    code = [signature]
    init_args = []
    if is_value:
        code.append('self._simple_schema_value = value_')
        init_args.append('value_')
    if is_object:
        args = ["'{0}': {0}".format(arg)
                for arg in (sorted(required) + sorted(props))]
        argdict = "{" + ', '.join(args) + "}"
        if allow_extra_kwds:
            code.append("kwds.update({0})".format(argdict))
        else:
            code.append("kwds = {0}".format(argdict))
        init_args.append('**kwds')
    code.append('super({classname}, self).__init__({args})'.format(classname=classname,
                                                                   args=', '.join(init_args)))
    return '\n    '.join(code)


class SchemaBaseMeta(type):
    """
    A metaclass for SchemaBase. The assumption is that each subclass of SchemaBase
    will be defined by its _json_schema attribute, which is a dict containing a
    valid JSON schema, and governs the way the class behaves.

    SchemaBaseMeta does two things:

    - if the class does not explicitly define an __init__() function, then
      define an appropriate __init__ function based on its _json_schema.

    - create a _schema_registry dict in the base class, and add each subclass
      to it, indexed by a unique hash computed from its _json_schema. This
      part is essential for the ``from_dict`` constructor, because it allows
      the constructor to quickly create an appropriate class hierarchy without
      having to hard-code all possibilities in the class definition.

    If you're unfamiliar with metaclasses, I have just the blog post for you:
    https://jakevdp.github.io/blog/2012/12/01/a-primer-on-python-metaclasses/
    """
    def __init__(cls, name, bases, dct):
        # Add init function if not defined explicitly in the class
        if '__init__' not in dct:
            schema = dct.get('_json_schema', {})
            # Because of the super() call, we need cls to be in global scope
            globals_ = {name: cls, 'Undefined': Undefined}
            code = init_code(schema, name)
            exec(code, globals_, dct)
            # The result of the executed function definition is in dct
            setattr(cls, '__init__', dct['__init__'])

        # Add this class to the registry
        if not hasattr(cls, '_schema_registry'):
            # this is the base class.  Initialize the registry
            cls._schema_registry = collections.defaultdict(list)
        else:
            # this is a derived class.  Add cls to the registry
            cls._schema_registry[cls._json_schema_hash()].append(cls)
        super(SchemaBaseMeta, cls).__init__(name, bases, dct)


@six.add_metaclass(SchemaBaseMeta)
class SchemaBase(object):
    """Base class for schema wrappers.

    Each derived class should set the _json_schema class attribute which is
    used for validation. If not specified in the class definition, an
    appropriate __init__ function will be generated by SchemaBaseMeta.
    """
    _simple_schema_value = Undefined
    _json_schema = {}
    _attr_names_to_ignore = ('_attr_names_to_ignore', '_json_schema',
                             '_schema_registry', '_simple_schema_value')

    # TODO: use getattr/getattribute & setattr to access properties? This may
    #       be cleaner overall than the _attr_names_to_ignore approach, but
    #       requires a bit of finesse (i.e. using object.__getattribute__ to
    #       prevent infinite recursion when looking up non-property members).
    #       Issue with the current approach is that if someone has a json schema
    #       with a property that is among the above names, this will silently
    #       ignore it.

    def __init__(self, *args, **kwds):
        # Two valid options for initialization, which should be handled by
        # derived classes:
        # - a single arg with no kwds, for, e.g. {'type': 'string'}
        # - zero args with zero or more kwds for {'type': 'object'}
        if len(args) == 1 and len(kwds) == 0:
            self._simple_schema_value = args[0]
        elif len(args) == 0:
            for key, val in kwds.items():
                setattr(self, key, val)
        else:
            raise ValueError("Multiple arguments must be passed by keyword")

    @classmethod
    def _json_schema_hash(cls):
        """Return a unique hash of this class' _json_schema"""
        return hash_schema(cls._json_schema)

    def __attrs(self):
        """Return a list of instance attributes"""
        members = inspect.getmembers(self, lambda a: not inspect.isroutine(a))
        return [name for name, val in members
                if not (name.startswith('__') and name.endswith('__'))
                and name not in self._attr_names_to_ignore]

    def __attr_dict(self):
        """return a dicitionary of attributes to values"""
        return {attr: getattr(self, attr) for attr in self.__attrs()}

    def to_dict(self, validate=True):
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
                return val.to_dict()
            else:
                return val

        dct = {attr: _todict(v) for attr, v in self.__attr_dict().items()
               if v is not Undefined}
        val = self._simple_schema_value

        if val is not Undefined and len(dct) > 0:
            raise ValueError("{0} instance has both a value and properties : "
                             "cannot serialize to dict")

        if val is Undefined:
            result = dct
        elif type(val) is dict:
            result = {attr: _todict(v) for attr, v in val.items()}
        elif type(val) is list:
            result = [_todict(v) for v in val]
        else:
            result = val
        if validate:
            jsonschema.validate(result, self._json_schema)
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
        # TODO: implement additionalProperties & patternProperties
        if validate:
            jsonschema.validate(dct, cls._json_schema)
        if isinstance(dct, dict):
            props = cls._json_schema.get('properties', {})
            hashes = {prop: hash_schema(val) for prop, val in props.items()}
            matches = {prop: cls._schema_registry[hash_]
                       for prop, hash_ in hashes.items()}

            # TODO: do something more than simply selecting the last match?
            wrappers = {prop: match[-1] for prop, match in matches.items() if match}
            kwds = {key: wrappers[key].from_dict(val) if key in wrappers else val
                    for key, val in dct.items()}
            return cls(**kwds)
        else:
            # TODO: if dct is a list, we need to find wrappers from
            #       the 'items' property of the schema
            return cls(dct)
