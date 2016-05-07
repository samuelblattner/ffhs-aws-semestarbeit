
"""
Module: AWD, Analysis, wissenschaftliches Rechnen und Datenvisualisierung
Course: BSc INF 2015, ZH5-Mo, FS16, Schuler Josef A.
This is my solution for the fourth of eight parts for the module at FFHS. This
is an implemenation of a spline plotter that interpolates individual points on
a given graph and draws the derivative.
"""
import numpy as np
from SplinePlotter import SplinePlotter


def e_fn(domain):
    return 1/np.power(np.e, domain)
e_fn.latex = r'$f(x)=\frac{1}{e^x}$'

SplinePlotter(domain_low=-5, domain_hi=5, lores=1.5, hires=0.5, fn=e_fn).draw()


def x_pow2(domain):
    return np.power(domain, 2)
x_pow2.latex = r'$f(x)=x^2$'

SplinePlotter(domain_low=-5, domain_hi=5, lores=1.5, hires=.1, fn=x_pow2).draw()


def x_pow3(domain):
    return np.power(domain, 3)
x_pow3.latex = r'$f(x)=x^3$'

SplinePlotter(domain_low=-5, domain_hi=5, lores=1, hires=.1, fn=x_pow3).draw()


def x_pow6(domain):
    return np.power(domain, 6)
x_pow6.latex = r'$f(x)=x^6$'

SplinePlotter(domain_low=-5, domain_hi=5, lores=1, hires=.1, fn=x_pow6).draw()


def sine(domain):
    return np.sin(domain)
sine.latex = r'$f(x)=sin(x)$'

SplinePlotter(domain_low=-5, domain_hi=5, lores=.1, hires=.01, fn=sine).draw()


def div_x_pow2(domain):
    return 1.0/np.power(domain, 2)
div_x_pow2.latex = r'$f(x)=\frac{1}{x^2}$'

SplinePlotter(domain_low=-1, domain_hi=1, value_max=1000, lores=0.01, hires=.005, fn=div_x_pow2).draw()


def div_sqrt_x(domain):
    return domain/np.sqrt(domain)
div_sqrt_x.latex = r'$f(x)=\frac{x}{\sqrt{x}}$'

SplinePlotter(domain_low=0.0001, domain_hi=2, lores=0.1, hires=.01, fn=div_sqrt_x).draw()
