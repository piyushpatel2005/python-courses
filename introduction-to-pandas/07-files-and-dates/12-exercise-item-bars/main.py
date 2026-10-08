import pandas as pd

def item_bars(frame):
    # Group items, sum units, then join one line per item.
    return ""

sample = pd.DataFrame({"item": ["Jam", "Tea", "Jam"], "units": [2, 1, 3]})
print(item_bars(sample))
