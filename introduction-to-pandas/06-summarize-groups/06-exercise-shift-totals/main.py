import pandas as pd

def shift_totals(a):
    return a["revenue"].copy()  # Replace this baseline.

a=pd.DataFrame({"market":["Harbor","Harbor","Park"],"shift":["AM","PM","AM"],"revenue":[12,8,4]})
print(shift_totals(a))
