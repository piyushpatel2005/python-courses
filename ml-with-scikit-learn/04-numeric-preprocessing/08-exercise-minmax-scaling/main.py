import numpy as np
from sklearn.preprocessing import MinMaxScaler
import pandas as pd


def range_scale(train, query):
    # Return the result described in the task.
    return None


# Supplied fixture and observation probe.
training = pd.read_csv("training.csv", float_precision="round_trip")
queries = pd.read_csv("queries.csv", float_precision="round_trip")
train = training[['feature_0', 'feature_1', 'feature_2']].to_numpy()
query = queries[['feature_0', 'feature_1', 'feature_2']].to_numpy()

result = range_scale(train, query)
if result is not None:
    scaler, values = result
    print("Training minima/maxima:", scaler.data_min_, scaler.data_max_)
    print("Query scaled values:\n", values)
else:
    print("Apply the training range without clipping queries.")
