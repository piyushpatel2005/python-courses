import pandas as pd

def older_revisions(frame):
    return frame.duplicated(subset=["order", "date"], keep="last")

def latest_revisions(frame):
    return frame.drop_duplicates(subset=["order", "date"], keep="last")

log = pd.DataFrame({"order": ["A", "A", "A"], "date": ["Fri", "Sat", "Fri"], "bags": [2, 3, 4]}, index=["old", "other-day", "new"])
print(older_revisions(log))
print(latest_revisions(log))
