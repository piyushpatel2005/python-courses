import pandas as pd

table = pd.DataFrame({"stall": ["Fern", "Bee", "Oak"], "baskets": [5, 3, 6], "aisle": ["east", "east", "west"]})
mask = (table["baskets"] >= 4) & (table["aisle"] == "east")
result = table.loc[mask]
print(result)
