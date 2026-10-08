import pandas as pd

ledger = pd.DataFrame({"stall": ["Fern", "Bee", "Oak"], "sales": [12, 18, 9], "zone": ["E", "W", "E"]}, index=["early", "mid", "late"])
position_window = ledger.iloc[0:2, 0:2]
result = ledger.loc["early":"mid", ["stall", "sales"]]
print(position_window)
print(result)
