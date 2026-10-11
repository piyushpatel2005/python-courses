import pandas as pd

def complete_ratings(frame, fallback):
    return frame.fillna({"rating": fallback})

inspections = pd.DataFrame({"stall": ["Oak", "Bee", "Fern"], "rating": [4, None, 5], "note": [None, "check sign", None]})
print(complete_ratings(inspections, 3))
