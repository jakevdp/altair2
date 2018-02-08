import sys
from os.path import abspath, join, dirname
sys.path.insert(0, abspath(join(dirname(__file__), '..')))

from datetime import datetime

from altair.schema import load_schema
from altair.schema.utils import SchemaInfo

FIELD_TEMPLATE = '''
class {classname}(wrapper.{basename}):
    """{classname} channel"""
    def __init__(self, field, **kwargs):
        kwds = parse_shorthand(field)
        kwds.update(kwargs)
        super({classname}, self).__init__(**kwds)
'''

VALUE_TEMPLATE = '''
class {classname}Value(wrapper.{basename}):
    """{classname} channel"""
    def __init__(self, value, *args, **kwargs):
        super({classname}Value, self).__init__(value=value, *args, **kwargs)
'''

def generate_channel_wrappers(schema, imports=None):
    if imports is None:
            imports = ["from altair.schema import wrapper",
                       "from altair.utils import parse_shorthand"]
    contents = ["# The contents of this file are automatically generated",
                "# at time {0}\n".format(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))]
    contents.extend(imports)
    contents.append('')

    encoding = SchemaInfo(schema['definitions']['EncodingWithFacet'])

    for prop, propschema in encoding.properties.items():
        if '$ref' in propschema:
            definitions = [propschema['$ref']]
        elif 'anyOf' in propschema:
            definitions = [s['$ref'] for s in propschema['anyOf'] if '$ref' in s]
        else:
            raise ValueError("either $ref or anyOf expected")
        for definition in definitions:
            basename = definition.split('/')[-1]
            classname = prop.title()
            if 'Value' in basename:
                template = VALUE_TEMPLATE
            else:
                template = FIELD_TEMPLATE
            contents.append(template.format(classname=classname,
                                            basename=basename))
    return '\n'.join(contents)


def main(outfile, imports=None):
    schema = load_schema()
    code = generate_channel_wrappers(schema, imports=imports)
    with open(outfile, 'w') as f:
        f.write(code)


if __name__ == '__main__':
    outfile = join(dirname(__file__), '..', 'altair', 'schema', 'channels.py')
    main(outfile)
