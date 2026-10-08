import pandas as pd

def older_revisions(frame):
    return pd.Series(False, index=frame.index)

def latest_revisions(frame):
    return frame.copy()

log = pd.DataFrame({"order": ["A", "A", "A"], "date": ["Fri", "Sat", "Fri"], "bags": [2, 3, 4]}, index=["old", "other-day", "new"])
print(older_revisions(log))
print(latest_revisions(log))
