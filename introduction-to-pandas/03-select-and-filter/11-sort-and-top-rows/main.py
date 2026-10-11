import pandas as pd

sales = pd.DataFrame({"stall": ["Fern", "Bee", "Oak"], "sales": [18, 30, 23]})
top_two = sales.nlargest(2, "sales")
result = sales.sort_values("sales", ascending=True)
print(result)
print(top_two)
