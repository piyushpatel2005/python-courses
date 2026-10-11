import pandas as pd

table = pd.DataFrame({"stall": ["tea", "jam"], "sold": [5, 11]}, index=[20, 10])
chosen = table.iloc[1, 1]
print(chosen)
print(table.loc[20, "sold"])
