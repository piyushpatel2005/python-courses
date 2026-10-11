import pandas as pd

def one_field(table, name):
    return None

def report_fields(table, names):
    return None

sample = pd.DataFrame({"stall": ["tea"], "sold": [3]})
print(one_field(sample, "sold"))
print(report_fields(sample, ["sold", "stall"]))
