class TablePrinter(object):
    rows = []

    def __init__(self, rows):
        self.rows = rows

    @staticmethod
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

    def print_as_table(self):
        """
        Prints the stored data as a table
        :return: None
        """
        # Find out the max length of every column
        column_max_lengths = [0 for cell in self.rows[0]]
        for row in self.rows:
            for c, cell in enumerate(row):
                len_cell = len(cell)
                if len_cell > column_max_lengths[c]:
                    column_max_lengths[c] = len_cell

        # Print row by row
        for row in self.rows:
            for c, column in enumerate(row):
                print(self.fill_with_space_to_length(column, column_max_lengths[c], align='right'), end=' ' * 5)
            print()
