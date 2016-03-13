class CSVParser(object):
    """
    This is a simple CSV parser class that is able to parse csv files and store
    their data in a two-dimensional list. Extend this class and override the
    sanitize method if you need more sophisticated finalizing of the data read.
    """
    # data
    rows = []

    def __init__(self, strip_spaces=False, separator=',', **kwargs):
        """
        Initializes the instance
        :param strip_spaces: If True, leading and trailing spaces will be stripped from the cell values
        :param separator: Separator by which cells are separated in the CSV
        :param kwargs: Use start_row, end_row, start_col, end_col to define the area that should be read in the CSV
        :return: None
        """
        self.separator = separator
        self.strip_spaces = strip_spaces
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
        if self.strip_spaces:
            return value.strip()
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
            file = open(path, 'r')
        except FileNotFoundError:
            print('The file "{}" does not exist!'.format(path))
            return False

        if file:
            lines = file.readlines()

            # If end_row hasn't been set, set it to the last row
            if not self.end_row:
                self.end_row = len(lines) - 1

            for line in lines[self.start_row:self.end_row]:
                # If end col hasn't been set, set it to the last col
                if not self.end_col:
                    self.end_col = len(line) - 1

                columns = [self.sanitize(cell) for cell in line.split(self.separator)[self.start_col:self.end_col]]
                self.rows.append(columns)
            return True

        else:
            return False
