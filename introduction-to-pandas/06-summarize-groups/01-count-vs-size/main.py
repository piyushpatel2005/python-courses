import pandas as pd

def zone_counts(a):
    return (a.groupby("zone")["amount"].count(),a.groupby("zone")["amount"].count())

a=pd.DataFrame({"zone":["North","North","South"],"amount":[10.0,None,6.0]})
print("Sums:",a.groupby("zone")["amount"].sum())
print("Means:",a.groupby("zone")["amount"].mean())
print(zone_counts(a))
