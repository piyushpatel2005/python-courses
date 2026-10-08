import pandas as pd

def daily_grid(a):
    return pd.pivot_table(a,index="zone",columns="day",values="amount",aggfunc="sum",fill_value=0)

a=pd.DataFrame({"zone":["N","N","S"],"day":["Fri","Sat","Fri"],"amount":[5,3,8]})
print(daily_grid(a))
