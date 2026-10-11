import pandas as pd

roster = pd.DataFrame({"stall": ["Fern", "Bee"], "zone": ["east", "west"], "fee": [20, 25]})
single_stall = roster["stall"]  # A Series, not a one-column DataFrame.
result = roster[["stall"]]
print(result)
