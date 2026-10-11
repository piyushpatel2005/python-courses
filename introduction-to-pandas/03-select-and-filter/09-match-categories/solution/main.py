import pandas as pd

stalls = pd.DataFrame({"name": ["Pear", "Loaf", "Soap"], "category": ["fruit", "bakery", "craft"]})
fruit_only = stalls.query("category == 'fruit'")
result = stalls.loc[stalls["category"].isin(["fruit", "bakery"])]
print(fruit_only)
print(result)
