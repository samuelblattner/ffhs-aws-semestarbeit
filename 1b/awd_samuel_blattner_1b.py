# -*- encoding:utf8 -*-
"""
Module: AWD, Analysis, wissenschaftliches Rechnen und Datenvisualisierung
Course: BSc INF 2015, ZH5-Mo, FS16, Schuler Josef A.
This is my solution for the second of eight parts for the module at FFHS. This
is an implemenation of a CSVParser class that loads csv-files and stores their
data in a two-dimensional list.
"""
from TablePrinter import TablePrinter
from CSVParser import CSVParser

parser = CSVParser(strip_spaces=True, start_row=2, start_col=0, end_col=10, end_row=20)
parser.load_from_csv('data.csv')
TablePrinter(parser.rows).print_as_table()

