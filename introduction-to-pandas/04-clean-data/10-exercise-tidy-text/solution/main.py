import pandas as pd

def tidy_registrations(frame):
    cleaned = frame.rename(columns={"host_name": "host"}).copy()
    cleaned["host"] = cleaned["host"].str.strip().str.lower()
    cleaned["dept"] = cleaned["dept"].replace({"arts": "creative"})
    return cleaned

registration = pd.DataFrame({"host_name": ["  ADA ", " Ben "], "dept": ["arts", "food"], "seats": [12, 8]})
print(tidy_registrations(registration))
