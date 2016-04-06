"""
Module: AWD, Analysis, wissenschaftliches Rechnen und Datenvisualisierung
Course: BSc INF 2015, ZH5-Mo, FS16, Schuler Josef A.
This is my solution for the third of eight parts for the module at FFHS. This
is an implemenation of a diagram plotter that can either draw curves or plot
data according to a two-dimensional list.
"""
from diagram import Diagram
from CSVParser import CSVParser


# Demo for Bars
csv_data_bars = []
csv_parser = CSVParser(strip_spaces=True, strip_inner_spaces=True, use_heading=True, use_labels=True)
csv_parser.data_type = float
csv_parser.load_from_csv('population.csv')
csv_data = csv_parser.rows
diagram_bars = Diagram(type='bars', data=csv_data)
diagram_bars.show()

# Demo for Piechart
csv_parser = CSVParser(strip_spaces=True, strip_inner_spaces=True, use_heading=True, use_labels=True)
csv_parser.data_type = float
csv_parser.load_from_csv('population.csv')
csv_data_piechart = csv_parser.rows
diagram_piechart = Diagram(type='piechart', data=csv_data_piechart)
diagram_piechart.show()

# Demo for Histogram
csv_parser = CSVParser(strip_spaces=True, strip_inner_spaces=True, use_heading=True, use_labels=True, start_col=1, end_col=14, start_row=9, end_row=81)
csv_parser.data_type = float
csv_parser.load_from_csv('temperatures.csv')
csv_data_histogram = csv_parser.rows
diagram_histogram = Diagram(type='histogram', data=csv_data_histogram, title='Temperaturen zwischen 1943 und 2015', x_label='Temperatur', y_label='Menge')
diagram_histogram.show()

# Demo for Curve
diagram_curve = Diagram(type='curve', data=[])
diagram_curve.show()
