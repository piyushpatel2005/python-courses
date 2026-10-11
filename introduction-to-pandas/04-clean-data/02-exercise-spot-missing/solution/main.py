import pandas as pd

def missing_addresses(frame):
    return frame["address"].isna()

def routable(frame):
    return frame.dropna(subset=["address"])

deliveries = pd.DataFrame({"parcel": ["D1", "D2", "D3"], "address": ["North gate", None, "Main hall"], "phone": [None, "555-0110", "555-0111"]}, index=["a", "b", "c"])
print(missing_addresses(deliveries))
print(routable(deliveries))
