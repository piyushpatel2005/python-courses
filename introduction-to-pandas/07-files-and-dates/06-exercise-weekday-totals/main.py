import pandas as pd

def visitors_by_weekday(frame):
    # Use frame["visited_on"].dt.day_name() as group labels.
    return pd.Series(dtype="int64")

sample = pd.DataFrame({"visited_on": pd.to_datetime(["2026-09-07", "2026-09-08", "2026-09-14"]), "visits": [3, 7, 5]})
print(visitors_by_weekday(sample))
