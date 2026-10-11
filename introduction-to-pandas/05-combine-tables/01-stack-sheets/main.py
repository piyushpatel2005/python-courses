import pandas as pd

def stack_sheets(a, b):
    return pd.concat([a, b], ignore_index=False)

a = pd.DataFrame({'stall': ['Lark'], 'crates': [2]}, index=[8])
b = pd.DataFrame({'stall': ['Moss'], 'crates': [4]}, index=[5])
print(stack_sheets(a, b))
