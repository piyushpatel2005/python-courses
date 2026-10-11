import pandas as pd

sales = pd.DataFrame({"stall": ["tea", "bread", "jam", "honey"], "sold": [3, 8, 5, 6]})
preview = sales.head(2)
print(preview)
print(sales.tail(2))
sales.info()
print(sales.describe())
