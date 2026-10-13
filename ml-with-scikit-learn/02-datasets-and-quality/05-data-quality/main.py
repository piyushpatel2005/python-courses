import numpy as np
import pandas as pd


def audit(table):
    return {"missing_fraction": float(table.isna().sum().sum()), "duplicate_rows": int(table.duplicated().sum()), "invalid_amounts": int((table["amount"] < 0).sum()), "positive_fraction": float(table["label"].mean())}


# Supplied fixture and observation probe.
table = pd.read_csv("observations.csv")

print("Audit:", audit(table))
print("Rows remain:", len(table))
