import pandas as pd

def stack_deliveries(a, b):
    return pd.concat([a, b], ignore_index=True)

def add_prices(a, b):
    return a.merge(b, on='product', how='left', validate='many_to_one')

def unpriced_count(ledger):
    return int(ledger['price'].isna().sum())

first = pd.DataFrame({'product': ['Tea'], 'units': [2]})
second = pd.DataFrame({'product': ['Jam'], 'units': [3]})
prices = pd.DataFrame({'product': ['Tea'], 'price': [4]})
combined = stack_deliveries(first, second)
ledger = add_prices(combined, prices)
print('Combined:', combined)
print('Ledger:', ledger)
print('Unpriced:', unpriced_count(ledger) if 'price' in ledger else 'price column not added yet')
