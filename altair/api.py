import six

import pandas as pd

from .schema import wrapper, channels, Undefined
from .utils import sanitize_dataframe, infer_vegalite_type


class TopLevelMixin(object):
    def _convert_data(self):
        if isinstance(self.data, six.string_types):
            # TODO: rewrite URLs for Vega/Vega-Lite examples?
            self.data = {'url': data}
        elif isinstance(self.data, pd.DataFrame):
            self.data = {'values': sanitize_dataframe(self.data).to_dict(orient='records')}
        elif self.data is None:
            pass
        elif self.data is Undefined:
            pass
        elif isinstance(self.data, dict):
            pass
        else:
            raise TypeError('Expected DataFrame, string, or dict, got: {0}'.format(new))

    def to_dict(self, *args, **kwargs):
        self._convert_data()
        return super(TopLevelMixin, self).to_dict(*args, **kwargs)

    def _ipython_display_(self):
        """Use the vega package to display in the classic Jupyter Notebook."""
        from IPython.display import display
        from vega3 import VegaLite
        display(VegaLite(self.to_dict(validate=True)))

    def display(self):
        """Display the Chart using the Jupyter Notebook's rich output.
        To use this in the classic Jupyter Notebook, the ``ipyvega`` package
        must be installed.
        To use this in JupyterLab/nteract, run the ``enable_mime_rendering``
        function first.
        """
        from IPython.display import display
        display(self)


class Chart(TopLevelMixin, wrapper.TopLevelFacetedUnitSpec):
    def __init__(self, data=Undefined, encoding=Undefined, mark=Undefined,
                 width=400, height=300, **kwargs):
        super(Chart, self).__init__(data=data, encoding=encoding, mark=mark,
                                    width=width, height=height, **kwargs)

    def mark_area(self, *args, **kwargs):
        self.mark = 'area'
        self.configure_mark(*args, **kwargs)
        return self

    def mark_bar(self, *args, **kwargs):
        self.mark = 'bar'
        self.configure_mark(*args, **kwargs)
        return self

    def mark_line(self, *args, **kwargs):
        self.mark = 'line'
        self.configure_mark(*args, **kwargs)
        return self

    def mark_point(self, *args, **kwargs):
        self.mark = 'point'
        self.configure_mark(*args, **kwargs)
        return self

    def mark_text(self, *args, **kwargs):
        self.mark = 'text'
        self.configure_mark(*args, **kwargs)
        return self

    def mark_tick(self, *args, **kwargs):
        self.mark = 'tick'
        self.configure_mark(*args, **kwargs)
        return self

    def mark_rect(self, *args, **kwargs):
        self.mark = 'rect'
        self.configure_mark(*args, **kwargs)
        return self

    def mark_rule(self, *args, **kwargs):
        self.mark = 'rule'
        self.configure_mark(*args, **kwargs)
        return self

    def mark_circle(self, *args, **kwargs):
        self.mark = 'circle'
        self.configure_mark(*args, **kwargs)
        return self

    def mark_square(self, *args, **kwargs):
        self.mark = 'square'
        self.configure_mark(*args, **kwargs)
        return self

    def mark_geoshape(self, *args, **kwargs):
        self.mark = 'geoshape'
        self.configure_mark(*args, **kwargs)
        return self

    def configure_mark(self, *args, **kwargs):
        if args or kwargs:
            if self.config is Undefined:
                self.config = wrapper.Config()
            self.config.mark = wrapper.MarkConfig(*args, **kwargs)
        return self

    def encode(self, *args, **kwargs):
        if args:
            raise NotImplementedError()
        for prop, field in list(kwargs.items()):
            if isinstance(field, six.string_types):
                col = self.data[field]
                type = infer_vegalite_type(col)
                cls = getattr(channels, prop.title())
                kwargs[prop] = cls(field=field, type=type)
        # TODO: don't overwrite old encodings?
        self.encoding = wrapper.EncodingWithFacet(*args, **kwargs)
        return self

    def interactive(self):
        """Make chart axes interactive"""
        self.selection = {'grid': {'bind': 'scales', 'type': 'interval'}}
        return self


class HConcatChart(TopLevelMixin, wrapper.TopLevelHConcatSpec):
    def __init__(self, hconcat, **kwargs):
        super(HConcatChart, self).__init__(hconcat=hconcat, **kwargs)


class VConcatChart(TopLevelMixin, wrapper.TopLevelVConcatSpec):
    def __init__(self, vconcat, **kwargs):
        super(VConcatChart, self).__init__(vconcat=vconcat, **kwargs)


class LayerChart(TopLevelMixin, wrapper.TopLevelLayerSpec):
    def __init__(self, layer, **kwargs):
        super(LayerChart, self).__init__(layer=layer, **kwargs)
