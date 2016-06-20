"""
Module: AWD, Analysis, wissenschaftliches Rechnen und Datenvisualisierung
Course: BSc INF 2015, ZH5-Mo, FS16, Schuler Josef A.
This is my solution for the eight of eight parts for the module at FFHS. This shows
some examples of how to visualize the "Kepler'sche Fassregel" and the "Trapezregel"
"""
from mpmath import arange
from sympy import *


x = Symbol('x')
domain = arange(-12, 12, 0.1)
function = x**3


def do_trapezregel(fn, N, a, b):
    """
    Calculate integral using the 'Trapezregel'. This function slices the domain in
    N equal portions and calculates their integrals. It also takes negative integrals
    into account and adds the corresponding zero-positions to the sections.
    :param fn: Function to integrate
    :param N: Number of slices (resolution)
    :param a: Left bound
    :param b: Right bound
    :return: Integral
    """
    title = 'Trapezregel:'
    print('\n\n{title}\n{underline}'.format(
        title=title,
        underline=len(title) * '='
    ))

    # Find 0-positions
    zero_positions = solve(fn, x)
    print('-> Zero positions found at x = ', zero_positions)
    sections = sorted(zero_positions + [a, b])
    print('-> Integrate sections: ', sections)

    section_integrals = []
    for cur_pos in range(0, len(sections) - 1):
        part_N = ceiling(N / len(sections))
        part_a = sections[cur_pos]
        part_b = sections[cur_pos + 1]
        step = (part_b - part_a) / part_N
        domain = [part_a + step * x_pos for x_pos in range(0, part_N + 1)]
        sum_function = sum([fn.subs({x: cur_x}) for cur_x in domain[1:-1]])
        integral = abs(float(((part_b - part_a) / (2 * part_N)) * (fn.subs({x: part_a}) + fn.subs({x: part_b}) + 2 * sum_function)))
        print('--> Integral of section {start} to {end}: {integral}'.format(
            start=part_a,
            end=part_b,
            integral=integral
        ))
        section_integrals.append(integral)

    # Calculate total integral
    sum_integral = sum(section_integrals)
    print('-' * 50)
    print('=> INTEGRAL: ', sum_integral)

    # Calculate max deviation from actual integral
    diff_fn = diff(fn, x, 2)
    max_error = (b - a) ** 3 / (12.0 * N ** 2) * max(abs(diff_fn.subs({x: a})), abs(diff_fn.subs({x: b})))
    print('=> Max. error:', max_error)
    return sum_integral


def do_simpsonregel(fn, a, b):
    """
    Calculates the integral of function fn using the 'Simpsonregel'.
    :param fn: Function to integrate
    :param a: Left bound
    :param b: Right bound
    :return: Integral
    """
    title = 'Simpsonregel:'
    print('\n\n{title}\n{underline}'.format(
        title=title,
        underline=len(title) * '='
    ))

    # Find 0-positions
    zero_positions = solve(fn, x)
    print('-> Zero positions found at x = ', zero_positions)
    sections = sorted(zero_positions + [a, b])
    print('-> Integrate sections: ', sections)

    # Find step size for N slices
    section_integrals = []
    for cur_pos in range(0, len(sections) - 1):
        part_a = sections[cur_pos]
        part_b = sections[cur_pos + 1]
        integral = abs(float((part_b - part_a) / 6.0 * (fn.subs({x: part_a}) + 4 * fn.subs({x: ((part_a + part_b) / 2)}) + fn.subs({x: part_b}))))
        print('--> Integral of section {start} to {end}: {integral}'.format(
            start=part_a,
            end=part_b,
            integral=integral
        ))
        section_integrals.append(integral)

    # Calculate total integral
    sum_integral = sum(section_integrals)
    print('-' * 50)
    print('=> INTEGRAL: ', sum_integral)

    # Calculate max deviation from actual integral
    diff_fn = diff(fn, x, 4)
    max_error = ((b - a) ** 5 / 2880.0) * max(abs(diff_fn.subs({x: a})), abs(diff_fn.subs({x: b})))
    print('=> Max error:', max_error)

    return sum_integral


def do_integration(fn, a, b):
    """
    Calculates the integral of function fn using Sympy integrate()
    :param fn: Function to integrate
    :param a: Left bound
    :param b: Right bound
    :return: Integral
    """
    title = 'True integral:'
    print('\n\n{title}\n{underline}'.format(
        title=title,
        underline=len(title) * '='
    ))

    # Find 0-positions
    zero_positions = solve(fn, x)
    print('-> Zero positions found at x = ', zero_positions)
    sections = sorted(zero_positions + [a, b])
    print('-> Integrate sections: ', sections)

    integrals = []
    for cur_pos in range(0, len(sections) - 1):
        a = sections[cur_pos]
        b = sections[cur_pos + 1]
        integral = abs(integrate(fn, (x, a, b)))
        print('-> Integral {a} to {b}: {result}'.format(
            a=a, b=b, result=integral
        ))
        integrals.append(integral)
    print('-' * 50)
    print('=> REAL INTEGRAL:', float(sum(integrals)))
    return float()

do_trapezregel(function, 20, -4, 4)
do_simpsonregel(function, -4, 4)
do_integration(function, -4, 4)


"""
Conclusion: The higher the resolution, the lower the max error in 'Trapezregel'. Simpsonregel for
max x**3 is exact. Play around with function = ... to experiment.
"""