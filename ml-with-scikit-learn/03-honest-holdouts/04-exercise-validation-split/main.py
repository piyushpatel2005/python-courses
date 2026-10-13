import numpy as np
from sklearn.model_selection import train_test_split
import pandas as pd


def three_way(ids):
    # Return the result described in the task.
    return None


# Supplied fixture and observation probe.
table = pd.read_csv("observations.csv", float_precision="round_trip")
ids = table["row_id"].to_numpy()
X = table[['feature_0', 'feature_1', 'feature_2']].to_numpy()
y = table["target"].to_numpy()

parts = three_way(ids)
if parts is not None:
    train, validation, test = parts
    print("Train/validation/test:", *(len(part) for part in parts))
    print("Training feature shape:", X[train].shape)
else:
    print("Reserve three disjoint row sets.")
