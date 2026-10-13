import numpy as np
from sklearn.model_selection import train_test_split
import pandas as pd


def split_rows(ids, X, y):
    # Return the result described in the task.
    return None


# Supplied fixture and observation probe.
table = pd.read_csv("observations.csv", float_precision="round_trip")
ids = table["row_id"].to_numpy()
X = table[['feature_0', 'feature_1', 'feature_2']].to_numpy()
y = table["target"].to_numpy()

parts = split_rows(ids, X, y)
if parts is not None:
    ids_train, ids_test, X_train, X_test, y_train, y_test = parts
    print("Train/test rows:", len(ids_train), len(ids_test))
    print("First held-out ID:", ids_test[0])
else:
    print("Split IDs, features, and targets together.")
