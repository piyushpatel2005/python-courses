from io import StringIO
import pandas as pd

def read_deliveries(text):
    return pd.read_csv(StringIO(text), parse_dates=["arrived_on"])

sample = "arrived_on,crate\n2026-09-01,Flowers\n2026-09-02,Herbs\n"
result = read_deliveries(sample)
print(result)
print(result.dtypes)
