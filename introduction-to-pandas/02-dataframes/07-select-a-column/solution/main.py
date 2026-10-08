import pandas as pd

table = pd.DataFrame({"stall": ["tea", "jam"], "sold": [3, 9], "price": [2, 4]})
chosen = table["sold"]
print(chosen)
print(table[["stall", "sold"]])
