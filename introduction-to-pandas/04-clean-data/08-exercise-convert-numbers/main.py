import pandas as pd

def numeric_cases(frame):
    return frame.copy()

inventory = pd.DataFrame({"item": ["Jam", "Rice", "Tea"], "cases": ["3", "unknown", "0"]}, index=["j", "r", "t"])
print(numeric_cases(inventory))
