class CSVParser(object):
    """
    This is a simple CSV parser class that is able to parse csv files and store
    their data in a two-dimensional list. Extend this class and override the
    sanitize method if you need more sophisticated finalizing of the data read.
    """
    # data
    rows = []
    data_type = str
    use_heading = False
    use_labels = False

    def __init__(self, strip_spaces=False, strip_inner_spaces=False, separator=',', **kwargs):
        """
        Initializes the instance
        :param strip_spaces: If True, leading and trailing spaces will be stripped from the cell values
        :param separator: Separator by which cells are separated in the CSV
        :param kwargs: Use start_row, end_row, start_col, end_col to define the area that should be read in the CSV
        :return: None
        """
        self.rows = []
        self.separator = separator
        self.strip_spaces = strip_spaces
        self.strip_inner_spaces = strip_inner_spaces
        self.start_row = kwargs.pop('start_row', 0)
        self.end_row = kwargs.pop('end_row', 0)
        self.start_col = kwargs.pop('start_col', None)
        self.end_col = kwargs.pop('end_col', None)

    def sanitize(self, value):
        """
        Is called for every cell read from the CSV-File. Override this method
        if you need to customize the way your data is processed.

        :param value: Value of the cell
        :return: Processed value
        """
        if self.strip_inner_spaces:
            return value.replace(' ', '')
        if self.strip_spaces:
            return value.strip()
        return value

    def convert_to_type(self, value, row, col):
        if row == 0 and self.use_heading or col == 0 and self.use_labels:
            return value
        try:
            return self.data_type(value)
        except ValueError:
            return value

    def load_from_csv(self, path):
        """
        Original task: Schreiben Sie eine Funktion, die eine csv Datei einliest und dabei eine zweidimensionale
        Python-Liste erstellt.
        Description: Loads data from csv and stores it in a two-dimensional list.

        :param path: Path to the csv-file
        :return: True if successful, False if not
        """
        try:
            file = open(path, 'r', encoding='utf-8')
        except FileNotFoundError:
            print('The file "{}" does not exist!'.format(path))
            return False

        if file:
            lines = file.readlines()

            # If end_row hasn't been set, set it to the last row
            if not self.end_row:
                self.end_row = len(lines) - 1

            for row, line in enumerate(lines[self.start_row:self.end_row + 1]):
                # If end col hasn't been set, set it to the last col
                if not self.end_col:
                    self.end_col = len(line) - 1

                columns = [self.convert_to_type(self.sanitize(cell), row, col) for col, cell in enumerate(line.split(self.separator)[self.start_col:self.end_col])]
                self.rows.append(columns)
            file.close()
            return True
        else:
            return False
