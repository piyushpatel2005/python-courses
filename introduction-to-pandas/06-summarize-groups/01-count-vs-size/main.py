import pandas as pd

def zone_counts(a):
    return (a.groupby('zone', observed=True, dropna=True)['amount'].count(), a.groupby('zone', observed=True, dropna=True)['amount'].count())

a = pd.DataFrame({'zone': ['North', 'North', 'South'], 'amount': [10.0, None, 6.0]})
print('Sums:', a.groupby('zone', observed=True, dropna=True)['amount'].sum())
print('Means:', a.groupby('zone', observed=True, dropna=True)['amount'].mean())
print(zone_counts(a))
