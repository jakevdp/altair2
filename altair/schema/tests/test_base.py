import jsonschema
import pytest

from .. import SchemaBase, Undefined
from ..base import hash_schema, UndefinedType, resolve_references


class Derived(SchemaBase):
    _json_schema = {
        'definitions': {
            'Foo': {
                'properties': {
                    'd': {'type': 'string'}
                }
            }
        },
        'additionalProperties': False,
        'properties': {
            'a': {'type': 'integer'},
            'b': {'type': 'string'},
            'c': {"$ref": "#/definitions/Foo"}
        }
    }


class Foo(SchemaBase):
    _json_schema = {
        "$ref": "#/definitions/Foo",
        'definitions': Derived._json_schema['definitions']
    }


class SimpleUnion(SchemaBase):
    _json_schema = {
        'anyOf' : [{'type': 'integer'}, {'type': 'string'}]
    }


class SimpleArray(SchemaBase):
    _json_schema = {
        'type': 'array',
        'items': {
            'anyOf' : [{'type': 'integer'}, {'type': 'string'}]
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

    with pytest.raises(TypeError):
        # no additional properties allowed
        Derived(foo='bar').to_dict()


def test_schema_hash():
    assert Foo._json_schema_hash() == hash_schema(Foo._json_schema)
    assert Derived._json_schema_hash() == hash_schema(Derived._json_schema)


def test_schema_hash_registry():
    for cls in [Derived, Foo]:
        hash_ = cls._json_schema_hash()
        assert cls in SchemaBase._schema_registry[hash_]


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
    assert SimpleUnion.from_dict('4')._simple_schema_value == '4'


def test_simple_array():
    assert SimpleArray([4, 5, 'six']).to_dict() == [4, 5, 'six']
    assert SimpleArray.from_dict(list('abc')).to_dict() == list('abc')


def test_undefined_singleton():
    assert Undefined is UndefinedType()


def test_resolve_references():
    schema = {
        '$ref': '#/definitions/Foo',
        'definitions': {
            'Foo': {'$ref': '#/definitions/Bar'},
            'Bar': {'$ref': '#/definitions/Baz'},
            'Baz': {'type': 'string'}
        }
    }
    assert resolve_references(schema) == {'type': 'string'}
