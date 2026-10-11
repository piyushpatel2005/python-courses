import pandas as pd

def rank_points(frame):
    return frame.copy()

def top_points(frame, count):
    return frame.iloc[:0].copy()

points = pd.DataFrame({"point": ["Gate", "Hall", "Yard"], "visits": [20, 11, 27]}, index=["g", "h", "y"])
print(rank_points(points))
print(top_points(points, 2))
