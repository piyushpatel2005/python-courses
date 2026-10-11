import pandas as pd

def shift_card(names, counts):
    return pd.Series(counts, index=names)

print(shift_card(["north", "south"], [3, 8]))
