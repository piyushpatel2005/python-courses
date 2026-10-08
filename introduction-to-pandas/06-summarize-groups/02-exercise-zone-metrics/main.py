import pandas as pd

def zone_metrics(a):
    return (a["amount"],)*4  # Replace this baseline.

a=pd.DataFrame({"zone":["Pier","Pier","Hill"],"amount":[8.0,None,12.0]})
print(zone_metrics(a))
