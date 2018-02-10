import jsonschema
import pytest

from .. import SchemaBase, schemaclass, Undefined
from ..core import UndefinedType


@schemaclass
class Derived(SchemaBase):
    __schema = {
        'definitions': {
            'Foo': {
                'type': 'object',
                'properties': {
                    'd': {'type': 'string'}
                }
            },
            'Bar': {'type': 'string', 'enum': ['A', 'B']}
        },
        'type': 'object',
        'additionalProperties': False,
        'properties': {
            'a': {'type': 'integer'},
            'b': {'type': 'string'},
            'c': {"$ref": "#/definitions/Foo"}
        }
    }


@schemaclass
class Foo(SchemaBase):
    __schema = {
        "$ref": "#/definitions/Foo",
        'definitions': Derived._Derived__schema['definitions']
    }


@schemaclass
class Bar(SchemaBase):
    __schema = {
        "$ref": "#/definitions/Bar",
        'definitions': Derived._Derived__schema['definitions']
    }


@schemaclass
class SimpleUnion(SchemaBase):
    __schema = {
        'anyOf' : [{'type': 'integer'}, {'type': 'string'}]
    }


@schemaclass
class DefinitionUnion(SchemaBase):
    __schema = {
        "anyOf": [
            {"$ref": "#/definitions/Foo"},
            {"$ref": "#/definitions/Bar"}
        ],
        "definitions": Derived._Derived__schema['definitions']
    }


@schemaclass
class SimpleArray(SchemaBase):
    __schema = {
        'type': 'array',
        'items': {
            'anyOf' : [{'type': 'integer'}, {'type': 'string'}]
        }
    }


@schemaclass(property_map=True)
class InvalidProperties(SchemaBase):
    __schema = {
        'type': 'object',
        'properties': {
            'for': {},
            'as': {},
            'vega-lite': {},
            '$schema': {}
        }
    }


def test_schema_cases():
    assert Derived(a=4, b='yo').to_dict() == {'a': 4, 'b': 'yo'}
    assert Derived(a=4, c={'d': 'hey'}).to_dict() == {'a': 4, 'c': {'d': 'hey'}}
    assert Derived(a=4, b='5', c=Foo('val')).to_dict() == {'a': 4, 'b': '5', 'c': {'d': 'val'}}
    assert Foo(d='hello', f=4).to_dict() == {'d': 'hello', 'f': 4}

    assert Derived().to_dict() == {}
    assert Foo().to_dict() == {}

    with pytest.raises(jsonschema.ValidationError):
        # a needs to be an integer
        Derived(a='yo').to_dict()

    with pytest.raises(jsonschema.ValidationError):
        # Foo.d needs to be a string
        Derived(c=Foo(4)).to_dict()

    with pytest.raises(jsonschema.ValidationError):
        # no additional properties allowed
        Derived(foo='bar').to_dict()


def test_round_trip():
    D = {'a': 4, 'b': 'yo'}
    assert Derived.from_dict(D).to_dict() == D

    D = {'a': 4, 'c': {'d': 'hey'}}
    assert Derived.from_dict(D).to_dict() == D

    D = {'a': 4, 'b': '5', 'c': {'d': 'val'}}
    assert Derived.from_dict(D).to_dict() == D

    D = {'d': 'hello', 'f': 4}
    assert Foo.from_dict(D).to_dict() == D


def test_from_dict():
    D = {'a': 4, 'b': '5', 'c': {'d': 'val'}}
    obj = Derived.from_dict(D)
    assert obj.a == 4
    assert obj.b == '5'
    assert isinstance(obj.c, Foo)


def test_simple_type():
    assert SimpleUnion(4).to_dict() == 4


def test_simple_array():
    assert SimpleArray([4, 5, 'six']).to_dict() == [4, 5, 'six']
    assert SimpleArray.from_dict(list('abc')).to_dict() == list('abc')


def test_definition_union():
    obj = DefinitionUnion.from_dict("A")
    assert isinstance(obj, Bar)
    assert obj.to_dict() == "A"

    obj = DefinitionUnion.from_dict("B")
    assert isinstance(obj, Bar)
    assert obj.to_dict() == "B"

    obj = DefinitionUnion.from_dict({'d': 'yo'})
    assert isinstance(obj, Foo)
    assert obj.to_dict() == {'d': 'yo'}


def test_invalid_properties():
    dct = {'for': 2, 'as': 3, 'vega-lite': 4, '$schema': 5}
    invalid = InvalidProperties.from_dict(dct)
    assert invalid['for'] == 2
    assert invalid['as'] == 3
    assert invalid['vega-lite'] == 4
    assert invalid['$schema'] == 5
    assert invalid.to_dict() == dct


def test_undefined_singleton():
    assert Undefined is UndefinedType()
