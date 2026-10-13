import numpy as np
from sklearn.preprocessing import StandardScaler
import pandas as pd


def scale_holdout(train, validation):
    scaler = StandardScaler().fit(train)
    return scaler, scaler.transform(validation)


# Supplied fixture and observation probe.
training = pd.read_csv("training.csv", float_precision="round_trip")
queries = pd.read_csv("queries.csv", float_precision="round_trip")
train = training[['weight_kg']].to_numpy()
validation = queries[['weight_kg']].to_numpy()

result = scale_holdout(train, validation)
if result is not None:
    scaler, values = result
    print("Fitted mean:", scaler.mean_)
    print("Validation values:", values)
else:
    print("Learn preprocessing only from training rows.")
