"""Generate a schema wrapper from a schema"""
import sys
import re
from datetime import datetime
from os.path import abspath, join, dirname
sys.path.insert(0, abspath(join(dirname(__file__), '..')))

from altair.schema import load_schema
from altair.schema.utils import get_valid_identifier


CLASS_TEMPLATE = '''
class {classname}({basename}):
    """{classname} schema wrapper"""
    _json_schema = {schema}
'''

class CodeSnippet(object):
    """Object whose repr() is the printed string"""
    def __init__(self, code):
        self.code = code

    def __repr__(self):
        return self.code


def _schema_class(classname, schema):
    return CLASS_TEMPLATE.format(classname=classname,
                                 basename='SchemaBase',
                                 schema=repr(schema))


def generate_schema_wrapper(schema, imports=None):
    if imports is None:
        imports = ["from altair.schema.base import SchemaBase",
                   "from altair.schema.loader import load_schema"]
    contents = ["# The contents of this file are automatically generated",
                "# at time {0}\n".format(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))]
    contents.extend(imports)
    contents.append('')
    contents.append(_schema_class('Root', CodeSnippet('load_schema()')))
    for name in schema['definitions']:
        pyname = get_valid_identifier(name)
        def_schema = {'$ref': '#/definitions/' + name,
                      'definitions': CodeSnippet("Root._json_schema['definitions']")}
        contents.append(_schema_class(pyname, def_schema))
    contents.append('')  # end with newline
    return '\n'.join(contents)


def main(outfile, imports=None):
    vl_schema = load_schema()
    base_import = 'from altair.schema.base import SchemaBase'
    file_contents = generate_schema_wrapper(vl_schema, imports)
    with open(outfile, 'w') as f:
        f.write(file_contents)


if __name__ == '__main__':
    outfile = join(dirname(__file__), '..', 'altair', 'schema', 'wrapper.py')
    main(outfile)
