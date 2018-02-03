import json
import os
from ._version import vegalite_version
from .base import BaseObject, Undefined


def load_schema():
    with open(os.path.join(os.path.dirname(__file__), 'vega-lite-schema.json')) as f:
        return json.load(f)
