import pandas as pd

def zone_metrics(a):
    g = a.groupby('zone', observed=True, dropna=True)['amount']
    return (g.mean(), g.sum(), g.count(), g.size())

a = pd.DataFrame({'zone': ['Pier', 'Pier', 'Hill'], 'amount': [8.0, None, 12.0]})
print(zone_metrics(a))
