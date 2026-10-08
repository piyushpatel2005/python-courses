import pandas as pd

def price_orders(a, b):
    return a.merge(b,on="product",how="left",validate="many_to_many")

a=pd.DataFrame({"product":["Bread","Bread"],"units":[1,2]})
b=pd.DataFrame({"product":["Bread"],"price":[4]})
print(price_orders(a, b))
