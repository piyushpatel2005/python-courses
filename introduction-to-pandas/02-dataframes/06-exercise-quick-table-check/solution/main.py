import pandas as pd

def ends(table, amount):
    return table.head(amount), table.tail(amount)

def numeric_summary(table):
    return table.describe()

sample = pd.DataFrame({"stock": [3, 5, 7], "price": [2, 4, 6]})
print(ends(sample, 1))
print(numeric_summary(sample))
