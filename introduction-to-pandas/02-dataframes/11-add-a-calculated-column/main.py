import pandas as pd

table = pd.DataFrame({"sold": [3, 6], "price": [5, 2]})
table["total"] = table["sold"] * table["price"]
print(table)
