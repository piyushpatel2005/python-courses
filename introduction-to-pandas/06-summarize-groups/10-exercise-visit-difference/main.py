import pandas as pd

def visit_difference(a):
    return a['visitors'].copy()

a = pd.DataFrame({'category': ['Food', 'Food', 'Art'], 'visitors': [10.0, 14.0, 7.0]})
print(visit_difference(a))
