import pandas as pd

stalls = pd.DataFrame({"stall": ["tea", "bread"], "visitors": [4, 9]})
records = pd.DataFrame([{"stall": "tea", "visitors": 4}, {"stall": "bread", "visitors": 9}])
print(stalls)
print(records)
