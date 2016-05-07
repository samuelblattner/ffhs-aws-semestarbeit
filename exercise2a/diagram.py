import matplotlib.pyplot as plt
import numpy as npy


class Diagram(object):
    """
    Diagram class as a wrapper for matplotlib to draw various graphs. Sublcass and implement
    your own _draw_<type> methods for custom graphs.

    """
    data = []
    range = None
    title = None
    type = 'piechart'
    x_label = None
    y_label = None

    class bcolors:
        """
        Inner utility class for text colors
        """
        HEADER = '\033[95m'
        OKBLUE = '\033[94m'
        OKGREEN = '\033[92m'
        WARNING = '\033[93m'
        FAIL = '\033[91m'
        ENDC = '\033[0m'
        BOLD = '\033[1m'
        UNDERLINE = '\033[4m'

    def __init__(self, *args, **kwargs):
        """
        Init method
        :param args:
        :param kwargs:
        :return:
        """
        self.title = kwargs.get('title', None)
        self.type = kwargs.get('type', 'piechart')
        self.data = kwargs.get('data', [])
        self.x_label = kwargs.get('x_label', [])
        self.y_label = kwargs.get('y_label', [])

    def show(self):
        """
        This method looks for a matching graph implementation for a given type.
         Raises error if no implementation found.
        :return:
        """
        fn = getattr(self, '_draw_{}'.format(self.type), None)
        if fn:
            plt.title(self.title if self.title else '')
            plt.xlabel(self.x_label if self.x_label else '')
            plt.ylabel(self.y_label if self.y_label else '')
            fn()
        else:
            raise NotImplementedError(
                'No draw function implemented for diagram type \'{diagram_type}\'. '
                'Base implementation of class Diagram implements the following diagram types: '
                '\'curve\', \'piechart\', \'bars\', \'hbars\', \'histogram\'. You can sublass Diagram and '
                'implement your own draw functions.'.format(
                    diagram_type=self.type
                ))

    @staticmethod
    def _get_function_parameters(param_list):
        """
        Prompts the user to enter all required parameters for
        a function of a given degree.
        :param param_list: A tuple of required parameters
        :return:
        """
        params = []
        for param_name, expected_type in param_list:
            parsed = False
            while not parsed:
                try:
                    params.append(expected_type(
                        input('{}: '.format(param_name))
                    ))
                    parsed = True
                except ValueError:
                    print('Cannot parse input. Expected type: {}'.format(expected_type))

        return params

    def _draw_curve(self):
        """
        Draws a polynomial of any degree. Parameters are entered interactively.
        :return:
        """
        print('\n\nDrawing polynomials\n================')
        degree = None
        while not degree:
            degree = input('Please enter the degree of the polynomial [default: 1]: ')
            if degree == '':
                degree = 1
            else:
                try:
                    degree = int(degree)
                except ValueError:
                    degree = None
                    print('{start_color}Unable to parse input. Please try again.{end_color}'.format(
                        start_color=self.bcolors.WARNING,
                        end_color=self.bcolors.ENDC
                    ))

        formula_string = ''
        param_letter_code = 97
        for deg in range(degree, 1, -1):
            formula_string += '{param_letter}x^{deg} + '.format(
                param_letter=chr(param_letter_code),
                deg=deg
            )
            param_letter_code += 1

        formula_string += '{param_letter}x + '.format(
            param_letter=chr(param_letter_code)
        )
        param_letter_code += 1
        formula_string += '{param_letter}'.format(
            param_letter=chr(param_letter_code)
        )

        print(
            '\n\nDrawing a polinome of the form: {start_color}{formula}{end_color} from '
            '{start_color}xmin{end_color} to {start_color}xmax{end_color}. '
            '\nPlease enter the parameters:'.format(
                formula=formula_string,
                start_color=self.bcolors.OKGREEN,
                end_color=self.bcolors.ENDC
            ))

        params = self._get_function_parameters(
            tuple(
                (chr(param_letter_code), float) for param_letter_code in range(97, 97 + degree + 1)
            ) +
            (('xMin', float),
             ('xMax', float))
        )

        # Draw
        self.range = npy.arange(params[-2], params[-1], .1)
        polynomials = [param * npy.power(self.range, power) for param, power in zip(params, range(degree, 1, -1))]
        y = sum(polynomials) + npy.multiply(self.range, params[-4]) + params[-3]
        plt.plot(self.range, y, "g-")

        plt.title('Function: $f(x) = {formula_string}$'.format(formula_string=formula_string), fontsize=20)
        plt.grid(True)
        plt.draw()
        plt.show()

    def _draw_piechart(self):
        """
        Draws a piechart
        :return:
        """
        self.range = npy.arange(0, 100)
        plt.pie(self.data[0])
        plt.show()

    def _draw_bars_base(self, first_column_is_legend=False, first_row_is_heading=False, vertical=True):
        """
        Shared bar drawing method for horizontal and vertical bars
        :param first_column_is_legend: Will treat first column as legend column if True
        :param first_row_is_heading: Will treat first row as heading row if True
        :return:
        """
        bar_fn = plt.bar if vertical else plt.barh
        colors = {
            0: 'g',
            1: 'r',
            2: 'c',
            3: 'm',
            4: 'y',
            5: 'k',
            6: 'r',
        }

        n_heading_row = 1 if first_row_is_heading else 0

        # Calculate bar width
        n_legend_col = 1 if first_column_is_legend else 0
        n_bars_per_group = len(self.data[0]) - n_legend_col
        bar_width = 1.0 / (n_bars_per_group + 2)

        # Set range to range of legend or just 0 to length of data
        if first_column_is_legend:
            self.range = npy.arange(self.data[0][0], self.data[-1][0] + 1, 1)
        else:
            self.range = npy.arange(0, len(self.data) - n_heading_row, 1)

        plt.grid(True)

        for n_col, data_col in enumerate(self.data[0][n_legend_col:]):
            color = colors.get(n_col % 6, 'g')

            bar_fn([row + (-n_bars_per_group / 2.0) * bar_width + n_col * bar_width for row in self.range],
                   [cols[n_col + n_legend_col] for cols in self.data[n_heading_row:]], width=bar_width, color=color)

        plt.show()

    def _draw_bars(self, first_column_is_legend=False, first_row_is_heading=False):
        """
        Draws vertical bars
        :return:
        """
        self._draw_bars_base(first_column_is_legend, first_row_is_heading)

    def _draw_hbars(self, first_column_is_legend=False, first_row_is_heading=False):
        """
        Draws horizontal bars
        :return:
        """
        self._draw_bars_base(first_column_is_legend, first_row_is_heading, vertical=False)

    def _draw_histogram(self):
        """
        Draws a histogram. This method flattens any two-dimensional list to display the values in a histogram.
        :return:
        """
        self.range = npy.arange(0, 100)
        all_data = [item for sublist in self.data for item in sublist]
        plt.hist(all_data)
        plt.show()
