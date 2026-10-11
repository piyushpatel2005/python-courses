import pandas as pd

def rank_points(frame):
    return frame.sort_values("visits", ascending=False)

def top_points(frame, count):
    return frame.nlargest(count, "visits")

points = pd.DataFrame({"point": ["Gate", "Hall", "Yard"], "visits": [20, 11, 27]}, index=["g", "h", "y"])
print(rank_points(points))
print(top_points(points, 2))
