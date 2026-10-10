import pandas as pd

def attach_bands(a, b):
    return a.copy()

a = pd.DataFrame({'band': ['A', 'B'], 'tables': [1, 2]})
b = pd.DataFrame({'fee': [5]}, index=['A'])
print(attach_bands(a, b))
