import pandas as pd

raw = pd.DataFrame({"vendor_name": ["  MINA ", " Sol "], "category": ["veg", "bread"]})
result = raw.rename(columns={"vendor_name": "vendor"})
result["vendor"] = result["vendor"].str.strip().str.lower()
result["category"] = result["category"].replace({"veg": "produce"})
print(result)
