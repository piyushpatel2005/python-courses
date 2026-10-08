import pandas as pd

def table_labels(table):
    return table.index.tolist(), table.columns.tolist()

def column_dtype(table, column):
    return table[column].dtype

sample = pd.DataFrame({"stall": ["tea"], "sold": [5]}, index=["morning"])
print(table_labels(sample), column_dtype(sample, "sold"))
