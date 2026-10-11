import pandas as pd

card = pd.Series([7, 14, 21], index=[20, 10, 30])
def first_count(values):
    return values.iloc[0]

chosen = first_count(card)
print(chosen)
