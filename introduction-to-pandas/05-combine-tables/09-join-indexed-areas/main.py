import pandas as pd

def attach_areas(a, b):
    return a.set_index('area').join(b, how='inner')

a = pd.DataFrame({'area': ['N', 'W'], 'stall': ['Lark', 'Elm']})
b = pd.DataFrame({'manager': ['Ada']}, index=['N'])
print(attach_areas(a, b))
