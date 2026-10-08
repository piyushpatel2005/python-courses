import pandas as pd

stock = pd.DataFrame({"item": ["Beans", "Tea", "Rice"], "units": [2, 8, 1], "status": ["ok", "ok", "ok"]}, index=["b", "t", "r"])
cleaned = stock.copy()
cleaned.loc[cleaned["units"] < 3, "status"] = "review"
print(cleaned)
