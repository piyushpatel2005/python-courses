import pandas as pd

roster = pd.DataFrame({"stall": ["Fern", "Bee"], "zone": ["east", "west"], "fee": [20, 25]})
single_stall = roster["stall"]
result = roster[["stall", "zone"]]
print(result)
