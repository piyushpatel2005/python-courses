import pandas as pd

def daily_gifts(a):
    return a.groupby(['zone', 'day'], observed=True, dropna=True)['amount'].sum()

a = pd.DataFrame({'zone': ['North', 'North', 'South'], 'day': ['Fri', 'Sat', 'Fri'], 'amount': [5, 7, 3]})
print('By zone:', a.groupby('zone', observed=True, dropna=True)['amount'].sum())
print(daily_gifts(a))
