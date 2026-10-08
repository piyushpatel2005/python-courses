import pandas as pd

def audit_badges(a, b):
    return a.copy()  # Replace this baseline.

a=pd.DataFrame({"badge":["E1","E2"],"time":[9,10]})
b=pd.DataFrame({"badge":["E2","E1"],"name":["Bo","Dee"]})
print(audit_badges(a, b))
