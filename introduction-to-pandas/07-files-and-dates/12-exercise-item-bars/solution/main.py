import pandas as pd

def item_bars(frame):
    totals = frame.groupby("item")["units"].sum().sort_index()
    return "\n".join(f"{name}: {'#' * int(count)}" for name, count in totals.items())

sample = pd.DataFrame({"item": ["Jam", "Tea", "Jam"], "units": [2, 1, 3]})
print(item_bars(sample))
