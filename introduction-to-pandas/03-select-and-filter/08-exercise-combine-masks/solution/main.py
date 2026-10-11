import pandas as pd

def priority_queue(frame, minimum):
    return frame.loc[(frame["hours"] >= minimum) & (frame["urgent"] == True)]

def review_queue(frame, minimum):
    return frame.loc[(frame["hours"] >= minimum) | (frame["urgent"] == True)]

requests = pd.DataFrame({"request": ["Signs", "Chairs", "Bins"], "hours": [4, 2, 5], "urgent": [True, True, False]}, index=["r1", "r2", "r3"])
print(priority_queue(requests, 4))
print(review_queue(requests, 4))
