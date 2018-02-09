"""
Utility routines
"""
import warnings
import re

import pandas as pd
import numpy as np

try:
    from pandas.api.types import infer_dtype
except ImportError: # Pandas before 0.20.0
    from pandas.lib import infer_dtype

from .schema import utils, wrapper

TYPECODE_MAP = {'ordinal': 'O',
                'nominal': 'N',
                'quantitative': 'Q',
                'temporal': 'T'}

INV_TYPECODE_MAP = {v: k for k, v in TYPECODE_MAP.items()}


def infer_vegalite_type(data, field=None):
    """
    From an array-like input, infer the correct vega typecode
    ('ordinal', 'nominal', 'quantitative', or 'temporal')
    Parameters
    ----------
    data: Numpy array or Pandas Series
    field: str column name
    """
    # See if we can read the type from the field
    if field is not None:
        parsed = parse_shorthand(field)
        if parsed.get('type'):
            return parsed['type']

    # Otherwise, infer based on the dtype of the input
    typ = infer_dtype(data)

    # TODO: implement a threshold to return 'ordinal'

    if typ in ['floating', 'mixed-integer-float', 'integer',
               'mixed-integer', 'complex']:
        return 'quantitative'
    elif typ in ['string', 'bytes', 'categorical', 'boolean', 'mixed', 'unicode']:
        return 'nominal'
    elif typ in ['datetime', 'datetime64', 'timedelta',
                 'timedelta64', 'date', 'time', 'period']:
        return 'temporal'
    else:
        warnings.warn("I don't know how to infer vegalite type from '{0}'.  "
                      "Defaulting to nominal.".format(typ))
        return 'nominal'


def parse_shorthand(shorthand):
    """
    Parse the shorthand expression for aggregation, field, and type.

    Parameters
    ----------
    shorthand: str
        Shorthand string of the form "agg(col):typ"

    Returns
    -------
    D : dict
        Dictionary which always contains a 'field' key, and additionally
        contains an 'aggregate' and 'type' key depending on the input.

    Examples
    --------
    >>> parse_shorthand('col')
    {'field': 'col'}

    >>> parse_shorthand('col:Q')
    {'field': 'col', 'type': 'quantitative'}

    >>> parse_shorthand('col:quantitative')
    {'field': 'col', 'type': 'quantitative'}

    >>> parse_shorthand('sum(col)')
    {'aggregate': 'sum', 'field': 'col'}

    >>> parse_shorthand('sum(col):Q')
    {'aggregate': 'sum', 'field': 'col', 'type': 'quantitative'}
    """
    if not shorthand:
        return {}

    # Must import this here to avoid circular imports
    valid_aggregates = utils.SchemaInfo(wrapper.AggregateOp).enum
    valid_typecodes = list(TYPECODE_MAP) + list(INV_TYPECODE_MAP)

    # build regular expressions
    units = dict(field='(?P<field>.*)',
                 type='(?P<type>{0})'.format('|'.join(valid_typecodes)),
                 aggregate='(?P<aggregate>{0})'.format('|'.join(valid_aggregates)))
    patterns = [r'{field}',
                r'{field}:{type}',
                r'{aggregate}\({field}\)',
                r'{aggregate}\({field}\):{type}']
    regexps = (re.compile('\A' + p.format(**units) + '\Z', re.DOTALL)
               for p in patterns[::-1])

    # find matches depending on valid fields passed
    match = next(exp.match(shorthand).groupdict() for exp in regexps
                 if exp.match(shorthand))

    # Use short form of the type expression
    typ = match.get('type', None)
    if typ:
        match['type'] = INV_TYPECODE_MAP.get(typ, typ)
    return match


def parse_shorthand_plus_data(shorthand, data):
    """Parse a field shorthand, and use data to infer type if not specified

    Parameters
    ----------
    shorthand: str
        Shorthand string of the form "agg(col):typ"
    data : pd.DataFrame
        Dataframe from which to infer types

    Returns
    -------
    D : dict
        Dictionary which always contains a 'field' key, and additionally
        contains an 'aggregate' and 'type' key depending on the input.

    Examples
    --------
    >>> data = pd.DataFrame({'foo': ['A', 'B', 'A', 'B'],
    ...                      'bar': [1, 2, 3, 4]})
    ...

    >>> parse_shorthand_plus_data('foo', data)
    {'field': 'foo', 'type': 'nominal'}

    >>> parse_shorthand_plus_data('bar', data)
    {'field': 'bar', 'type': 'quantitative'}

    >>> parse_shorthand_plus_data('bar:O', data)
    {'field': 'bar', 'type': 'ordinal'}

    >>> parse_shorthand_plus_data('sum(bar)', data)
    {'aggregate': 'sum', 'field': 'bar', 'type': 'quantitative'}
    """
    attrs = parse_shorthand(shorthand)
    if 'type' not in attrs:
        field = attrs['field']
        if not isinstance(data, pd.DataFrame):
            raise ValueError("type must be specified unless data is provided "
                             "in the form of a dataframe")
        col = data[field]
        attrs['type'] = infer_vegalite_type(col)
    return attrs

def sanitize_dataframe(df):
    """Sanitize a DataFrame to prepare it for serialization.
    * Make a copy
    * Raise ValueError if it has a hierarchical index.
    * Convert categoricals to strings.
    * Convert np.bool_ dtypes to Python bool objects
    * Convert np.int dtypes to Python int objects
    * Convert floats to objects and replace NaNs by None.
    * Convert DateTime dtypes into appropriate string representations
    """
    df = df.copy()

    if isinstance(df.index, pd.core.index.MultiIndex):
        raise ValueError('Hierarchical indices not supported')
    if isinstance(df.columns, pd.core.index.MultiIndex):
        raise ValueError('Hierarchical indices not supported')

    def to_list_if_array(val):
        if isinstance(val, np.ndarray):
            return val.tolist()
        else:
            return val

    for col_name, dtype in df.dtypes.iteritems():
        if str(dtype) == 'category':
            # XXXX: work around bug in to_json for categorical types
            # https://github.com/pydata/pandas/issues/10778
            df[col_name] = df[col_name].astype(str)
        elif str(dtype) == 'bool':
            # convert numpy bools to objects; np.bool is not JSON serializable
            df[col_name] = df[col_name].astype(object)
        elif np.issubdtype(dtype, np.integer):
            # convert integers to objects; np.int is not JSON serializable
            df[col_name] = df[col_name].astype(object)
        elif np.issubdtype(dtype, np.floating):
            # For floats, convert nan->None: np.float is not JSON serializable
            col = df[col_name].astype(object)
            df[col_name] = col.where(col.notnull(), None)
        elif str(dtype).startswith('datetime'):
            # Convert datetimes to strings
            # astype(str) will choose the appropriate resolution
            df[col_name] = df[col_name].astype(str).replace('NaT', '')
        elif dtype == object:
            # Convert numpy arrays saved as objects to lists
            # Arrays are not JSON serializable
            col = df[col_name].apply(to_list_if_array, convert_dtype=False)
            df[col_name] = col.where(col.notnull(), None)
    return df


def use_signature(Obj):
    """Apply call signature and documentation of Obj to the decorated method"""
    def decorate(f):
        # call-signature of f is exposed via __wrapped__.
        # we want it to mimic Obj.__init__
        f.__wrapped__ = Obj.__init__
        f._uses_signature = Obj

        # Supplement the docstring of f with information from Obj
        doclines = Obj.__doc__.splitlines()
        if not f.__doc__:
            f.__doc__ = ""
        f.__doc__ += '\n'.join(doclines[1:])
        return f
    return decorate
