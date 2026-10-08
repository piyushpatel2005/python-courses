import pandas as pd

def delivery_days(frame):
    return frame["arrived_on"].dt.month

sample = pd.DataFrame({"arrived_on": pd.to_datetime(["2026-09-04", "2026-09-18"])})
print(delivery_days(sample).tolist())
