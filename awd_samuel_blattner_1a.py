# -*- encoding: utf8 -*-
"""
Module: AWD, Analysis, wissenschaftliches Rechnen und Datenvisualisierung
Course: BSc INF 2015, ZH5-Mo, FS16, Schuler Josef A.
This is my solution for the first of eight parts for the module at FFHS. This is a simple tool to
examine various approaches of calculating Fibonacci numbers and their execution times.
"""
import math
from time import time


def fibonacci_rec_simple(n):
    """
    Original task: Eine naive Implementierung setzt die obige Rekursionsgleichung direkt um.

    Description: This is a straight-forward recursive function that calculates the Fibonacci-values in
    a simple way. However, it does not account for the fact that values are calculated
    multiple times. E.g. fibonacci_rec_simple(5) will calculate n-1 and n-2, so 4 and 3. But then,
    fibonacci_rec_simple(4) will calculate 3 and 2, even though 3 is already being calculated by 5. With
    high numbers, this way is very inefficient.

    :param n: Position in the Fibonacci-Sequence to be calculated
    :return: Value of the Fibonacci-Sequence at the position specified
    """
    if n < 2:
        return 1
    return fibonacci_rec_simple(n-1) + fibonacci_rec_simple(n-2)


def fibonacci_rec_simple_counted(n):
    """
    Original task: Schreiben Sie eine weitere Python-Funktion, die berechnet, wie viele Funktionsaufrufe
    von fib notwendig sind, um die n-te Fibonacci-Zahl zu berechnen.

    Description: This is an extension of the function fibonacci_rec_simple above and additionally tracks
    how many recursive function calls are necessary to calculate the value.

    :param n: Position in the Fibonacci-Sequence to be calculated
    :return: A tuple containing the actual value of the Fibonacci-Sequence at the position specified and
    the amount of recursive function calls.
    """
    if n < 2:
        return 1, 1
    sum1, recursive_count1 = fibonacci_rec_simple_counted(n-1)
    sum2, recursive_count2 = fibonacci_rec_simple_counted(n-2)
    # Count this function (1 + ...) plus the amounts of the recursive calls
    return sum1 + sum2, 1 + recursive_count1 + recursive_count2


def fibonacci_rec_single_drill(n):
    """
    Original task: Implementieren Sie eine weitere Python-Funktion zur Berechnung der n-ten Fibonacci-Zahl,
    die möglichst effizient ist. (Hinweis: das kann rekursiv oder iterativ gelöst werden.)

    Description: This function avoids multiple calculations by 'drilling down' in one single path and by
    retrieving the values of all levels of recursion it crosses on its way down. Every level will return both,
    its own value and the value of one level further down the path. It will then calculate the value of every level
    on its way back up.

    :param n: Position in the Fibonacci-Sequence to be calculated
    :return: A tuple containing the value for the current level, the amount of function calls and
    the value of the previous level.
    """
    if n < 1:
        return 1, 1, 0
    value_current_level, count, value_prev_level = fibonacci_rec_single_drill(n-1)
    return value_prev_level + value_current_level, count + 1, value_current_level


hash_table = {}


def fibonacci_rec_hashed(n):
    """
    Original task: Implementieren Sie eine weitere Python-Funktion zur Berechnung der n-ten Fibonacci-Zahl,
    die möglichst effizient ist. (Hinweis: das kann rekursiv oder iterativ gelöst werden.)

    Description: This function uses the same algorithm as the first function but stores calculated values
    in a hash table. So, whenever a value should be calculated the hashed value takes precedence over
    recalculating the value. This way, multiple calculations for one value can be avoided.

    :param n: Position in the Fibonacci-Sequence to be calculated
    :return: A tuple containing the value at the position specified and the number of function calls.
    """
    if n < 2:
        return 1, 1

    hashed_value, count = hash_table.get(n, (False, 1))
    if hashed_value:
        return hashed_value, 1

    # Look up the value in the hash table
    sum2, count1 = fibonacci_rec_hashed(n-2)
    sum1, count2 = fibonacci_rec_hashed(n-1)
    result = sum1 + sum2
    hash_table.setdefault(n, (result, 0))
    return result, count + count1 + count2


def fibonacci_iter_simple(n):
    """
    Original task: Implementieren Sie eine weitere Python-Funktion zur Berechnung der n-ten Fibonacci-Zahl,
    die möglichst effizient ist. (Hinweis: das kann rekursiv oder iterativ gelöst werden.)

    Description: This function is an iterative way of calculating the Fibonacci sequence.

    :param n: Position in the Fibonacci-Sequence to be calculated
    :return: A tuple containing the value at the position specified and the number of function calls.
    """
    sum1 = 0
    sum2 = 1
    sum3 = 1
    for i in range(0, n):
        sum3 = sum1 + sum2
        sum1 = sum2
        sum2 = sum3
    return sum3, 1


def fibonacci_moivre_binet(n):
    """
    Original task: Implementieren Sie eine weitere Python-Funktion zur Berechnung der n-ten Fibonacci-Zahl,
    die möglichst effizient ist. (Hinweis: das kann rekursiv oder iterativ gelöst werden.)

    Description: This function uses the Moivre-Binet Formula to calculate Fibonacci numbers. See
    https://en.wikipedia.org/wiki/Fibonacci_number for reference.

    Note: This function delivers imprecise results at high n's due to the limited capability of the
    computer to deal with infinite fractions!

    :param n: Position in the Fibonacci-Sequence to be calculated
    :return: A tuple containing the value at the position specified and the number of function calls.
    """
    try:
        import decimal
        decimal.getcontext().prec = 100
        sqrt_5 = decimal.Decimal(5).sqrt()
    except:
        sqrt_5 = math.sqrt(5)

    n += 1
    return round(((1/sqrt_5) * (((1 + sqrt_5) / 2) ** n) - ((1 - sqrt_5) / 2) ** n), 0), 1


def fill_with_space_to_length(string_to_fill, new_length, align='left'):
    """
    Fills a given string with empty spaces to the desired length. String
    can be aligned left (default) or right. Returns the unchanged string
    if new_length is equal to or less than the length of the string.

    :param string_to_fill: The string that should be 'filled'
    :param new_length: The final length of the string
    :param align: Align string 'left' or 'right'
    :return: Filled string
    """
    delta = new_length - len(string_to_fill)
    if delta > 0:
        if align == 'left':
            return string_to_fill + ' ' * delta
        return ' ' * delta + string_to_fill
    return string_to_fill


def print_function_stats(measurements):
    """
    Prints the function stats in a table
    :param measurements: List of measurements of the function calls
    :return: void
    """
    if len(measurements):
        columns = [['Function'], ['Calculated value'], ['Calculation time'], ['Function calls'], ['Efficiency']]

        # Find the best execution time for efficiency calculations
        execution_times = [calc_time for fn_name, value, calc_time, calls in measurements if calc_time >= 0]
        best_exec_time = min(execution_times)

        # Fill columns with values
        for fn_name, value, calc_time, calls in measurements:
            columns[0].append(fn_name)
            columns[1].append(str(value))
            columns[2].append('%0.10f ms' % calc_time if calc_time >= 0 else '-')
            columns[3].append(str(calls))
            columns[4].append('%3.4f%%' % (1 / (calc_time / best_exec_time) * 100) if calc_time >= 0 else '-')

        print('\n')

        # Print table
        for row in range(0, len(measurements)+1):
            total_row_length = 0
            for c, column in enumerate(columns):
                align = 'right' if c > 0 else 'left'
                max_length = len(max(column, key=lambda s: len(s))) + 5
                print(fill_with_space_to_length(column[row], max_length, align=align), end='')
                total_row_length += max_length

            print('')
            if row == 0:
                print('=' * total_row_length)

    else:
        print('No measurements received!')


def measure_efficiency(function_list, fib_pos):
    """
    Executes the functions of function_list and measures the amount of time every
    function takes to complete. Prints the values in a table afterwards.
    :param measurements: List of functions to be called
    :param fib_pos: Position of the Fibonacci sequence to be calculated
    :return: void
    """
    measurements = []

    for fn in function_list:
        start = time()
        try:
            result = fn(fib_pos)

            if type(result) is tuple:
                value = result[0]
                calls = result[1]
            else:
                calls = 'N/A'
                value = result

        except RuntimeError:
            calls = 'Recursion limit exceeded!'
            value = 'N/A'
        except:
            print('Error calling {}. Skipping...'.format(fn.__name__))
            measurements.append(
                [fn.__name__, '-', -1, '-']
            )
            continue

        end = time()
        measurements.append(
            [fn.__name__, value, (end-start), calls]
        )

    print_function_stats(measurements)


fib_pos = int(input('\nWhich position of the Fibonacci sequence should be calculated? '))
print('Calculating, please wait ...')
measure_efficiency(
    [
        fibonacci_rec_simple,
        fibonacci_rec_simple_counted,
        fibonacci_rec_single_drill,
        fibonacci_rec_hashed,
        fibonacci_iter_simple,
        fibonacci_moivre_binet
    ],
    fib_pos
)
