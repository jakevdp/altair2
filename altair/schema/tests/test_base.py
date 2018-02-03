import jsonschema
import pytest

from .. import BaseObject, Undefined


class Derived(BaseObject):
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


class Foo(BaseObject):
    _json_schema = {
        "$ref": "#/definitions/Foo",
        'definitions': Derived._json_schema['definitions']
    }

    def __init__(self, d=Undefined, **kwds):
        kwds['d'] = d
        super(Foo, self).__init__(**kwds)


def test_schema_cases():
    assert Derived(a=4, b='yo').to_dict() == {'a': 4, 'b': 'yo'}
    assert Derived(a=4, c={'d': 'hey'}).to_dict() == {'a': 4, 'c': {'d': 'hey'}}
    assert Derived(a=4, b='5', c=Foo('val')).to_dict() == {'a': 4, 'b': '5', 'c': {'d': 'val'}}
    assert Foo(d='hello', f=4).to_dict() == {'d': 'hello', 'f': 4}

    assert Derived().to_dict() == {}
    assert Foo().to_dict() == {}

    with pytest.raises(jsonschema.ValidationError):
        # no additional properties allowed
        Derived(foo='bar').to_dict()

    with pytest.raises(jsonschema.ValidationError):
        # a needs to be an integer
        Derived(a='yo').to_dict()

    with pytest.raises(jsonschema.ValidationError):
        # Foo.d needs to be a string
        Derived(c=Foo(4)).to_dict()
