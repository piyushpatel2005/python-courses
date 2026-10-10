import pandas as pd

def visit_profile(a):
    return (a['visitors'].describe(), a['type'].value_counts(dropna=False))

a = pd.DataFrame({'type': ['Produce', 'Art', None], 'visitors': [20.0, None, 8.0]})
print(visit_profile(a))
