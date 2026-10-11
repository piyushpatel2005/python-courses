import pandas as pd

def with_revenue(table):
    return None

sample = pd.DataFrame({"sold": [2, 5], "price": [3, 4]}, index=["tea", "jam"])
print(with_revenue(sample))
