import numpy as np
from sklearn.model_selection import train_test_split
import pandas as pd


def stratified_ids(ids, labels):
    return train_test_split(ids, test_size=0.25, random_state=17)


# Supplied fixture and observation probe.
table = pd.read_csv("labels.csv", dtype={"row_id": "int32", "label": "int32"})
ids = table["row_id"].to_numpy(dtype=np.intp)
labels = table["label"].to_numpy(dtype=np.intp)

parts = stratified_ids(ids, labels)
if parts is not None:
    train, test = parts
    print("Train counts:", np.bincount(labels[train]))
    print("Test counts:", np.bincount(labels[test]))
else:
    print("Split while preserving class shares.")
