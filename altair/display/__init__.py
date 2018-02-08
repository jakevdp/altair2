from .mixins import VegaDisplayMixin
from . import utils


class VegaLite(VegaDisplayMixin):
    def __init__(self, spec, data=None):
        self.spec = spec
        self.data = data

    def _get_spec_info(self):
        spec = utils.prepare_vegalite_spec(self.spec, self.data)
        return (spec, 'vega-lite')


class Vega(VegaDisplayMixin):
    def __init__(self, spec, data=None):
        self.spec = spec
        self.data = data

    def _get_spec_info(self):
        spec = utils.prepare_vega_spec(self.spec, self.data)
        return (spec, 'vega')
