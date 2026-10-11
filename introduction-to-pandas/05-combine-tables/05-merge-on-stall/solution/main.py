import pandas as pd

def attach_vendors(a, b):
    return a.merge(b, on='stall', how='left')

a = pd.DataFrame({'stall': ['Lark', 'Unknown'], 'tables': [2, 1]})
b = pd.DataFrame({'stall': ['Lark'], 'vendor': ['Ari']})
print(attach_vendors(a, b))
