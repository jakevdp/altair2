"""Tools to download relevant files from Vega-Lite"""

import os
import sys
import shutil
import zipfile
import io
from urllib import request


VEGALITE_VERSION = "2.1.1"
VEGALITE_RELEASE = "https://github.com/vega/{library}/archive/v{version}.zip"
SCHEMA_URL = "https://vega.github.io/schema/{library}/v{version}.json"
ALTAIR_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__),
                                           '..', 'altair'))
EXAMPLE_PATH = os.path.join(ALTAIR_PATH, 'examples', 'spec')
SCHEMA_PATH = os.path.join(ALTAIR_PATH, "schema")

                              
def download_vegalite_schema(version=VEGALITE_VERSION):
    version = str(version)
    url = SCHEMA_URL.format(library='vega-lite', version=version)
    if not os.path.exists(SCHEMA_PATH):
        os.makedirs(SCHEMA_PATH)
    outpath = os.path.join(SCHEMA_PATH, "vega-lite-schema.json")
    print("downloading {0} -> {1}".format(url, outpath))
    request.urlretrieve(url, outpath)


def download_vegalite_examples(version=VEGALITE_VERSION):
    response = request.urlopen(VEGALITE_RELEASE.format(library='vega-lite',
                                                       version='2.1.1'))
    z = zipfile.ZipFile(io.BytesIO(response.read()))
    
    if not os.path.exists(EXAMPLE_PATH):
        os.makedirs(EXAMPLE_PATH)
        
    for filename in os.listdir(EXAMPLE_PATH):
        if filename.endswith('.vl.json'):
            os.remove(os.path.join(EXAMPLE_PATH, filename))

    for f in z.namelist():
        path = f.split('/')
        if len(path) == 4:
            if path[1] == 'examples' and path[3].endswith('.vl.json'):
                outfile = os.path.join(EXAMPLE_PATH, path[3])
                print("{0} -> {1}".format(path[3], outfile))
                with z.open(f) as zf, open(outfile, 'wb') as out:
                    shutil.copyfileobj(zf, out)


if __name__ == '__main__':
    download_vegalite_schema()
    download_vegalite_examples()


    
    
