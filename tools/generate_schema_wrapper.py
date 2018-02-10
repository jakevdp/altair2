"""Generate a schema wrapper from a schema"""
import sys
import re
from datetime import datetime
from os.path import abspath, join, dirname
sys.path.insert(0, abspath(join(dirname(__file__), '..')))

from schemapi.codegen import schema_class, CodeSnippet
from schemapi.utils import get_valid_identifier, SchemaInfo
from altair.schema import load_schema


def generate_schema_wrapper(schema):
    schema = load_schema()
    contents = ["# The contents of this file are automatically generated",
                "# at time {0}\n".format(datetime.now().strftime('%Y-%m-%d %H:%M:%S')),
                "from altair.schema.base import SchemaBase, Undefined",
                "from altair.schema.loader import load_schema",
                ""]
    contents.append(schema_class('Root', schema, CodeSnippet('load_schema()')))
    for name in schema['definitions']:
        pyname = get_valid_identifier(name)
        defschema = {'$ref': '#/definitions/' + name,
                     'definitions': schema['definitions']}
        defschema_repr = {'$ref': '#/definitions/' + name,
                          'definitions': CodeSnippet("Root._Root__schema['definitions']")}

        contents.append(schema_class(pyname, defschema, defschema_repr))
    contents.append('')  # end with newline
    return '\n'.join(contents)


def main(outfile):
    vl_schema = load_schema()
    file_contents = generate_schema_wrapper(vl_schema)
    with open(outfile, 'w') as f:
        f.write(file_contents)


if __name__ == '__main__':
    outfile = join(dirname(__file__), '..', 'altair', 'schema', 'wrapper.py')
    main(outfile)
