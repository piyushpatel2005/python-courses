import numpy as np
import pandas as pd


def checkout_features(table):
    # Return the result described in the task.
    return None


# Supplied fixture and observation probe.
table = pd.read_csv("orders.csv")

result = checkout_features(table)
if result is not None:
    print("Checkout columns:", list(result.columns))
    print(result.iloc[:2])
else:
    print("Select only information known at checkout.")
