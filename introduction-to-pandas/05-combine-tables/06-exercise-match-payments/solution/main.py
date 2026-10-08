import pandas as pd

def match_payments(a, b):
    return a.merge(b,on="ticket",how="left")

a=pd.DataFrame({"ticket":["T4","T5"],"seats":[2,1]})
b=pd.DataFrame({"ticket":["T4"],"paid":[True]})
print(match_payments(a, b))
