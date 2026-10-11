import pandas as pd

def visit_difference(a):
    return a['visitors'] - a.groupby('category', observed=True, dropna=True)['visitors'].transform('mean')

a = pd.DataFrame({'category': ['Food', 'Food', 'Art'], 'visitors': [10.0, 14.0, 7.0]})
print(visit_difference(a))
