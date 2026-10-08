import pandas as pd

def align_notes(a, b):
    return pd.concat([a,b],axis=1)

a=pd.DataFrame({"visits":[12,8]},index=["Mon","Tue"])
b=pd.DataFrame({"weather":["dry","wet"]},index=["Tue","Wed"])
print(align_notes(a, b))
