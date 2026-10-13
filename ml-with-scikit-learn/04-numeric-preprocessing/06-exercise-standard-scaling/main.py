import numpy as np
from sklearn.preprocessing import StandardScaler
import pandas as pd


def standardize(train, query):
    # Return the result described in the task.
    return None


# Supplied fixture and observation probe.
training = pd.read_csv("training.csv", float_precision="round_trip")
queries = pd.read_csv("queries.csv", float_precision="round_trip")
train = training[['feature_0', 'feature_1', 'feature_2']].to_numpy()
query = queries[['feature_0', 'feature_1', 'feature_2']].to_numpy()

result = standardize(train, query)
if result is not None:
    scaler, values = result
    print("Training mean:", scaler.mean_)
    print("Training scale:", scaler.scale_)
    print("Query z values:\n", values)
else:
    print("Center and scale using training statistics.")
