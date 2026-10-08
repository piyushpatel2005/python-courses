import pandas as pd

def attach_bands(a, b):
    if not b.index.is_unique:
        raise ValueError("Duplicate fee-band keys")
    return a.set_index("band").join(b,how="left")

a=pd.DataFrame({"band":["A","B"],"tables":[1,2]})
b=pd.DataFrame({"fee":[5]},index=["A"])
print(attach_bands(a, b))
