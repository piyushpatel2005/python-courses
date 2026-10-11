import pandas as pd

def priority_queue(frame, minimum):
    return frame.iloc[:0].copy()

def review_queue(frame, minimum):
    return frame.iloc[:0].copy()

requests = pd.DataFrame({"request": ["Signs", "Chairs", "Bins"], "hours": [4, 2, 5], "urgent": [True, True, False]}, index=["r1", "r2", "r3"])
print(priority_queue(requests, 4))
print(review_queue(requests, 4))
