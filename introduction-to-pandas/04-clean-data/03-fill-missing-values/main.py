import pandas as pd

sessions = pd.DataFrame({"session": ["Music", "Repair", "Seed swap"], "attendees": [12, None, 8], "comment": [None, "extra chairs", None]})
result = sessions.fillna({"attendees": -1})
print(result)
