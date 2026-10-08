import pandas as pd

def align_fees(a, b):
    return pd.concat([a,b],axis=1)

a=pd.DataFrame({"jars":[4,6]},index=["A1","B2"])
b=pd.DataFrame({"fee":[12,15]},index=["B2","C3"])
print(align_fees(a, b))
