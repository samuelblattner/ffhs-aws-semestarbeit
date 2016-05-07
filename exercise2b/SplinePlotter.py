import matplotlib.pyplot as plt
import numpy as np
from scipy import interpolate


class SplinePlotter(object):
    """
    Main class SplinePlotter receives parameters to draw the
    interpolated graphs.
    """
    domain_lower_bound = -5
    domain_upper_bound = 5
    lores_domain = []
    hires_domain = []
    value_max = 100
    fn = lambda x: x

    def __init__(self, *args, **kwargs):
        lores = kwargs.get('lores', 1)
        hires = kwargs.get('hires', .1)
        self.value_max = kwargs.get('value_max', self.value_max)
        self.domain_lower_bound = kwargs.get('domain_low', self.domain_lower_bound)
        self.domain_upper_bound = kwargs.get('domain_hi', self.domain_upper_bound)
        self.lores_domain = np.arange(self.domain_lower_bound, self.domain_upper_bound, lores)
        self.hires_domain = np.arange(self.domain_lower_bound, self.domain_upper_bound, hires)
        self.fn = kwargs.get('fn', self.fn)
        self.lores_values = self.fn(self.lores_domain)
        self.hires_values = self.fn(self.hires_domain)

    def _set_axis_range(self):
        """
        Set graph area based on graph that should be drawn. Add 20% of domain and value range on each side.
        :return:
        """
        domain_extension = (self.domain_upper_bound - self.domain_lower_bound) * 0.2
        value_extension = (min(max(self.lores_values), self.value_max) - min(self.lores_values)) * 0.2
        plt.axis([self.domain_lower_bound - domain_extension, self.domain_upper_bound + domain_extension,
                  min(self.lores_values) - value_extension, min(max(self.lores_values), self.value_max) + value_extension])

    def draw(self):
        """
        Draws the control points, connects them with lines, draws the interpolated representation and
        finally shows the derivative.
        :return:
        """
        # Generate spline representation
        tck = interpolate.splrep(self.lores_domain, self.lores_values, s=0)
        interpolated_values = interpolate.splev(self.hires_domain, tck, der=0)
        derivative_values = interpolate.splev(self.hires_domain, tck, der=1)
        plt.plot(
            self.lores_domain, self.lores_values, 'gx',  # control points
            self.lores_domain, self.lores_values,  # linear
            self.hires_domain, interpolated_values, 'r',  # interpolation
            self.hires_domain, derivative_values, 'c',  # derivative
            self.hires_domain, self.fn(self.hires_domain),  # actual function
        )

        self._set_axis_range()
        fn_name = self.fn.latex if hasattr(self.fn, 'latex') else self.fn.__name__
        plt.legend(['Control points', 'Linear', 'Cubic Spline', 'Derivative', 'Function ' + fn_name, ], fontsize=20)
        plt.grid(True)
        plt.show()
