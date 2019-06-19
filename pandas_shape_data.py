import pandas as pd

data = pd.read_csv("test.csv", engine="python", sep='ぉ', quotechar='ぉ',
                   error_bad_lines=False)

data.to_csv('pd_shape_data.csv')
