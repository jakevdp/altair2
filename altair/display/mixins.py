import json
import uuid
import pkgutil

from IPython.display import display, publish_display_data


class VegaDisplayMixin(object):
    """A Mixin to display Vega or Vega-Lite data"""
    def _get_spec_info(self):
        """
        Should return a tuple of (spec, render_type)
        - spec is a Python dictionary
        - and render_type is 'vega' or 'vega-lite'
        """
        raise NotImplementedError()

    def _generate_html(self, id):
        template = pkgutil.get_data('vega3', 'static/vega.html')
        template = template.decode('UTF-8')
        return template.format(id=id)

    def _generate_js(self, id, spec, render_type, **kwds):
        template = pkgutil.get_data('vega3', 'static/vega.js')
        template = template.decode('UTF-8')
        return template.format(
            selector='#{0}'.format(id),
            spec=json.dumps(spec, **kwds),
            type=render_type
        )

    def _ipython_display_(self):
        """Display the visualization in the Jupyter notebook."""
        spec, render_type = self._get_spec_info()

        id = uuid.uuid4()
        publish_display_data(
            {'text/html': self._generate_html(id)},
            metadata={'jupyter-vega3': '#{0}'.format(id)}
        )
        publish_display_data(
            {'application/javascript':
                self._generate_js(id, spec, render_type)},
            metadata={'jupyter-vega3': '#{0}'.format(id)}
        )

    def display(self):
        """Render the visualization."""
        display(self)
