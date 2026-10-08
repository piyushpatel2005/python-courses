import pandas as pd

def from_columns(columns):
    return pd.DataFrame(columns)

def from_records(records):
    return pd.DataFrame(records)

print(from_columns({"item": ["apple"], "count": [3]}))
print(from_records([{"item": "pear", "count": 2}]))
