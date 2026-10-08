import pandas as pd

counts = pd.DataFrame({"station": ["Gate", "Hall", "Yard"], "tickets": ["12", "oops", "9"]})
result = pd.to_numeric(counts["tickets"], errors="coerce").fillna(0).astype(int)
print(result)
