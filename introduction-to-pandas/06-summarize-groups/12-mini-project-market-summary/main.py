import pandas as pd

def revenue_grid(a):
    return a.copy()  # Replace this baseline.

def zone_report(a):
    return a.copy()  # Replace this baseline.

def missing_amounts(a):
    return 0  # Replace this baseline.

sales=pd.DataFrame({"zone":["Pier","Pier","Hill"],"day":["Fri","Sat","Fri"],"amount":[6.0,4.0,None]})
print("Grid:",revenue_grid(sales))
print("Report:",zone_report(sales))
print("Unrecorded:",missing_amounts(sales))
