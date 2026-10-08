import pandas as pd

def missing_addresses(frame):
    return pd.Series(False, index=frame.index, name="address")

def routable(frame):
    return frame.copy()

deliveries = pd.DataFrame({"parcel": ["D1", "D2", "D3"], "address": ["North gate", None, "Main hall"], "phone": [None, "555-0110", "555-0111"]}, index=["a", "b", "c"])
print(missing_addresses(deliveries))
print(routable(deliveries))
