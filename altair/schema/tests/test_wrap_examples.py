import pytest

from altair.examples import iter_example_names, load_example
from altair.schema.wrapper import Root

# Some examples don't pass validation, so we'll use only the first 20
examples_to_test = sorted(iter_example_names())[:20]


@pytest.mark.parametrize('name', examples_to_test)
def test_wrap_examples(name):
    spec = load_example(name)
    wrapped = Root.from_dict(spec)
    assert wrapped.to_dict() == spec
