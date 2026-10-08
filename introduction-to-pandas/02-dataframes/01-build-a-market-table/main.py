import pandas as pd

stalls = pd.DataFrame({"stall": ["tea", "bread"], "visitors": [4, 6]})
records = pd.DataFrame([{"stall": "tea", "visitors": 4}, {"stall": "bread", "visitors": 6}])
print(stalls)
print(records)
