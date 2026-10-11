import pandas as pd

def tidy_registrations(frame):
    cleaned = frame.copy()
    # Rename host_name to host here.
    # Strip and lowercase host values here.
    # Replace the department code here.
    return cleaned

registration = pd.DataFrame({"host_name": ["  ADA ", " Ben "], "dept": ["arts", "food"], "seats": [12, 8]})
print(tidy_registrations(registration))
