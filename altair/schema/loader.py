import json
from os.path import join, dirname


def load_schema():
    """Load the vega-lite schema included with the package"""
    with open(join(dirname(__file__), 'vega-lite-schema.json')) as f:
        return json.load(f)
