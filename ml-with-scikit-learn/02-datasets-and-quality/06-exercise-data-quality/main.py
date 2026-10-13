import numpy as np
import pandas as pd


def audit(table):
    # Return the result described in the task.
    return None


# Supplied fixture and observation probe.
table = pd.read_csv("orders.csv")

print("Audit:", audit(table))
print("Rows remain:", len(table))
