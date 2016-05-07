"""
Module: AWD, Analysis, wissenschaftliches Rechnen und Datenvisualisierung
Course: BSc INF 2015, ZH5-Mo, FS16, Schuler Josef A.
This is my solution for the fifth of eight parts for the module at FFHS. This
is an implemenation of the Newton method to calculate x-Axis interception.
"""
from sympy import *
from sympy.parsing.sympy_parser import parse_expr


max_iterations = 30


def calculate_intersection(function, derivative, x0):
    """
    Calculates the x position of the intersection of a given function
    with the x-axis. Executes max_iterations iterations to reach
    an approximation of the real intersection point.
    :param function: A sympy expression
    :param derivative: The derivative of the expression
    :param x0: Starting x position
    :return: Approximated x position of the intersection
    """
    global max_iterations
    consumed_iterations = 0
    n_sign_switches = 0

    x = Symbol('x')
    x1 = 0

    # Loop until max_iterations have been reached
    while consumed_iterations < max_iterations:
        x1 = float(x0 - function.subs({x: x0}) / derivative.subs({x: x0}))
        print('x0 = {} -> x1 = {} | x-distance: {}'.format(float(x0), float(x1), float(abs(x1 - x0))))

        # Count sign switches. If there are too many the expression most
        # probably does not have any intersections with the x-axis
        if x1 * x0 < 0:
            n_sign_switches += 1

        if consumed_iterations > 0 and n_sign_switches > 5:
            print('Switching signs too often. This function probably has no intersections '
                  'with the X-Axis within the bounds indicated.')
            return None

        consumed_iterations += 1
        x0 = x1
    return x1


def newtonize(function, bounds):
    """
    Wrapper function to use the Newton-Method on a given expressions within
    given bounds.
    :param function: A Sympy expression
    :param bounds: Tuple of lower and upper bounds
    :return: None
    """
    derivative = diff(function)

    title = 'Newtonizing...'
    print('\n{}\n{}\n'.format(title, '-' * len(title)))

    x0 = bounds[0]
    title = 'Narrowing down from lower bound {}'.format(x0)
    print('\n{}\n{}'.format(title, '-' * len(title)))
    x1 = calculate_intersection(function, derivative, x0)
    if x1:
        print('Intersection with x-axis at x ~', float(x1))

    x0 = bounds[1]
    title = 'Narrowing down from upper bound {}'.format(x0)
    print('\n{}\n{}'.format(title, '-' * len(title)))
    x1 = calculate_intersection(function, derivative, x0)
    if x1:
        print('Intersection with x-axis at x ~', float(x1))

parsed_expression = parse_expr(input('Please enter the right part of f(x) = ... : '))
left_bound = int(input('Please enter the left bound of x: '))
right_bound = int(input('Please enter the right bound of x: '))


title = 'Finding x-axis intersections using Newtons\'s method'
print('\n\n{}\n{}'.format(title, '=' * len(title)))
newtonize(parsed_expression, (left_bound, right_bound))
