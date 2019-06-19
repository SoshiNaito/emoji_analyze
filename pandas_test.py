import pandas
from pandas.io.parsers import _make_parser_function

data = pandas.read_csv("test.csv")

print(data)