import pandas as pd

def numeric_cases(frame):
    cleaned = frame.copy()
    cleaned["cases"] = pd.to_numeric(cleaned["cases"], errors="coerce").astype("Int64")
    return cleaned

inventory = pd.DataFrame({"item": ["Jam", "Rice", "Tea"], "cases": ["3", "unknown", "0"]}, index=["j", "r", "t"])
print(numeric_cases(inventory))
