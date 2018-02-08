from .mixins import VegaDisplayMixin
from . import utils


class VegaLite(VegaDisplayMixin):
    def __init__(self, spec, data=None):
        self.spec = spec
        self.data = data

    def _get_spec_and_data(self):
        return (self.spec, self.data, 'vega-lite')

    def _prepare_spec(self, spec, data):
        return utils.prepare_vegalite_spec(spec, data)


class Vega(VegaDisplayMixin):
    def __init__(self, spec, data=None):
        self.spec = spec
        self.data = data

    def _get_spec_and_data(self):
        return (self.spec, self.data, 'vega-lite')

    def _prepare_spec(self, spec, data):
        return utils.prepare_vega_spec(spec, data)
