import pandas as pd

def zone_baseline(a):
    return a.groupby('zone', observed=True, dropna=True)['amount'].transform('mean')

a = pd.DataFrame({'zone': ['North', 'North', 'South'], 'amount': [4.0, 8.0, 9.0]})
print(zone_baseline(a))
