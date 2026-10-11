import pandas as pd

signups = pd.DataFrame({"name": ["Ada", "Bea", "Cy"], "email": ["ada@example.test", None, "cy@example.test"], "note": [None, "near gate", "has cart"]}, index=["a", "b", "c"])
missing = signups.isna()
result = signups.dropna(subset=["email"])
print(missing)
print(result)
