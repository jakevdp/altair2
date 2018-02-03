import os
import json


def iter_example_names():
    specdir = os.path.join(os.path.dirname(__file__), 'spec')
    for spec in sorted(os.listdir(specdir)):
        yield spec


def load_example(name):
    filename = os.path.join(os.path.dirname(__file__), 'spec', name)
    with open(filename, 'r') as f:
        return json.load(f)


def iter_example_json():
    for name in iter_example_names():
        return load_example(name)
