import pandas as pd

def visit_profile(a):
    return (a['visitors'], a['type'])

a = pd.DataFrame({'type': ['Produce', 'Art', None], 'visitors': [20.0, None, 8.0]})
print(visit_profile(a))
