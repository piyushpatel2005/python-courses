import pandas as pd

visits = pd.DataFrame({"stall": ["Bee", "Bee", "Bee"], "day": ["Fri", "Sat", "Fri"], "note": ["first", "second", "repeat"]})
repeat_mask = visits.duplicated(subset=["stall", "day"])
result = visits.drop_duplicates(subset=["stall"])
print(repeat_mask)
print(result)
