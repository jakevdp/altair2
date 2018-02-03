import jsonschema

import pytest

from .. import iter_example_names, load_example
from ...schema import load_schema


@pytest.fixture
def schema():
    return load_schema()


@pytest.mark.parametrize('name', iter_example_names())
def test_example_json(name, schema):
    spec = load_example(name)
    jsonschema.validate(spec, schema)
        
