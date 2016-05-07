"""
Module: AWD, Analysis, wissenschaftliches Rechnen und Datenvisualisierung
Course: BSc INF 2015, ZH5-Mo, FS16, Schuler Josef A.
This is my solution for the fifth of eight parts for the module at FFHS. This
is a visualization of the Taylor-Polynomial.
"""
import math
import matplotlib.pyplot as plt
import numpy as npy
from sympy import diff, Symbol
from sympy.parsing.sympy_parser import parse_expr


def get_derivatives(function, num_derivatives):
    """
    Helper function to retrieve num_derivatives derivatives for
    the function 'function'.
    :param function: Function for which to find derivatives
    :param num_derivatives: Number of derivatives to get
    :return: A list of derivatives for the given function
    """
    derivatives = [diff(function)]
    cur_derivative = 1
    valid = True
    while valid and cur_derivative < num_derivatives:
        derivative = diff(derivatives[cur_derivative-1])
        if derivative != 0:
            derivatives.append(diff(derivatives[cur_derivative-1]))
            cur_derivative += 1
        else:
            valid = False

    return derivatives


def caluclate_taylor_for_x(x_center, x_val, function, derivatives, num_levels):
    """
    Calculates the corresponding y-value for a given value x_val in
    respect of the common x_center using the Taylor-Polynomial with num_levels levels.
    :param x_center: Common x center
    :param x_val: Current x value
    :param derivatives: List of function derivatives including the origin function at index 0
    :param num_levels: Number of levels to caluclate
    :return: y value
    """
    x = Symbol('x')
    y = function.subs({x: x_center})
    for l in range(0, num_levels):
        y += derivatives[l].subs({x: x_center}) / math.factorial(l + 1) * ((x_val - x_center) ** (l + 1))

    return y


parsed_expression = parse_expr(input('Please enter the right part of f(x) = ... : '))
num_levels = int(input('How many levels of the Taylor-Polynomial would you like to develop? '))
left_bound = int(input('Please enter the left bound of x: '))
right_bound = int(input('Please enter the right bound of x: '))

derivatives = get_derivatives(parsed_expression, num_levels)
print(derivatives)
domain = npy.arange(left_bound, right_bound, .1)
colors = {
    0: 'g',
    1: 'r',
    2: 'c',
    3: 'm',
    4: 'y',
    5: 'k',
    6: 'r',
}

x = Symbol('x')
plt.plot(domain, [parsed_expression.subs({x: x_val}) for x_val in domain], 'g-', linewidth=4)

for l in range(1, len(derivatives)+1):
    plt.plot(domain, [caluclate_taylor_for_x(0, x, parsed_expression, derivatives, l) for x in domain],
             "{}-".format(colors.get(l % 6)))

plt.grid(True)
plt.show()
