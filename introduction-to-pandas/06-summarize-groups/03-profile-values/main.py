import pandas as pd

def profile_sales(a):
    return a["amount"].describe(),a["category"].value_counts(dropna=True)

a=pd.DataFrame({"category":["Food",None,"Food","Craft"],"amount":[5.0,7.0,9.0,11.0]})
print(profile_sales(a))
