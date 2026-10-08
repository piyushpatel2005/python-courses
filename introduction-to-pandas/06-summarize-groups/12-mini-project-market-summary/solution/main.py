import pandas as pd

def revenue_grid(a):
    return pd.pivot_table(a,index="zone",columns="day",values="amount",aggfunc="sum",fill_value=0)

def zone_report(a):
    return a.groupby("zone").agg(revenue=("amount","sum"),entries=("amount","size"))

def missing_amounts(a):
    return int(a["amount"].isna().sum())

sales=pd.DataFrame({"zone":["Pier","Pier","Hill"],"day":["Fri","Sat","Fri"],"amount":[6.0,4.0,None]})
print("Grid:",revenue_grid(sales))
print("Report:",zone_report(sales))
print("Unrecorded:",missing_amounts(sales))
