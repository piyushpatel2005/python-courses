import pandas as pd

def stack_visits(a, b):
    return pd.concat([a, b], ignore_index=True)

a = pd.DataFrame({'stall': ['Fern'], 'visits': [3]}, index=[9])
b = pd.DataFrame({'stall': ['Ash'], 'visits': [8]}, index=[2])
print(stack_visits(a, b))
