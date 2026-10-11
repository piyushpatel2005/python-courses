import pandas as pd

stock = pd.DataFrame({"stall": ["Fern", "Bee", "Oak"], "crates": [5, 8, 12]}, index=["f", "b", "o"])
def select_stalls(frame):
    mask = frame["crates"] >= 5
    return mask, frame.loc[mask]

mask, result = select_stalls(stock)
print(mask)
print(result)
