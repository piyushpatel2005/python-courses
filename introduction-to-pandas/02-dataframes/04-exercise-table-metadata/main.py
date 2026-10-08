import pandas as pd

def table_labels(table):
    return None

def column_dtype(table, column):
    return None

sample = pd.DataFrame({"stall": ["tea"], "sold": [5]}, index=["morning"])
print(table_labels(sample), column_dtype(sample, "sold"))
