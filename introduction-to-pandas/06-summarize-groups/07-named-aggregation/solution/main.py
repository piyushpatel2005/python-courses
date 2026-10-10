import pandas as pd

def vendor_report(a):
    return a.groupby('vendor', observed=True, dropna=True).agg(average=('total', 'mean'), orders=('total', 'size'))

a = pd.DataFrame({'vendor': ['Lark', 'Lark', 'Moss'], 'total': [4.0, 10.0, 6.0]})
print(vendor_report(a))
