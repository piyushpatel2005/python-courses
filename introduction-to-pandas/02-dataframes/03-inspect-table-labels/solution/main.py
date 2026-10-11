import pandas as pd

table = pd.DataFrame({"stall": ["tea", "honey"], "sold": [5, 8]}, index=["early", "late"])
print(table.index.tolist())
print(table.columns.tolist())
print(table.dtypes)
