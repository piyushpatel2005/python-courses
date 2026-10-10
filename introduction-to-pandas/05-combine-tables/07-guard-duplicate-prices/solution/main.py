import pandas as pd

def price_orders(a, b):
    return a.merge(b, on='product', how='left', validate='many_to_one')

a = pd.DataFrame({'product': ['Bread', 'Bread'], 'units': [1, 2]})
b = pd.DataFrame({'product': ['Bread'], 'price': [4]})
print(price_orders(a, b))

try:
    duplicate_prices = pd.concat([b, b], ignore_index=True)
    print("Duplicate lookup rows:", len(price_orders(a, duplicate_prices)))
except pd.errors.MergeError:
    print("Duplicate price lookup rejected")
