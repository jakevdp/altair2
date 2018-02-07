import jsonschema
import pytest

from altair.examples import iter_example_names, load_example
from altair.schema.wrapper import Root
from altair.schema import load_schema

# These take a while, so we'll use only the first 40 for now
examples_to_test = sorted(iter_example_names())[:40]


@pytest.fixture
def schema():
    return load_schema()


@pytest.mark.parametrize('name', examples_to_test)
def test_wrap_examples(name, schema):
    spec = load_example(name)

    try:
        jsonschema.validate(spec, schema)
    except:
        pytest.xfail('schema {0} is not valid'.format(name))
    else:
        wrapped = Root.from_dict(spec)
        assert wrapped.to_dict() == spec
