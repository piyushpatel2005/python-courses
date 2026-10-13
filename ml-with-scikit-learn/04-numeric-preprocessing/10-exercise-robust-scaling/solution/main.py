import numpy as np
from sklearn.preprocessing import RobustScaler, StandardScaler
import pandas as pd


def robust_scale(train, query):
    scaler = RobustScaler(quantile_range=(25, 75)).fit(train)
    return scaler, scaler.transform(query)


# Supplied fixture and observation probe.
training = pd.read_csv("training.csv", float_precision="round_trip")
queries = pd.read_csv("queries.csv", float_precision="round_trip")
train = training[['width_cm', 'volume_l']].to_numpy()
query = queries[['width_cm', 'volume_l']].to_numpy()

result = robust_scale(train, query)
if result is not None:
    scaler, values = result
    print("Chosen scaling:\n", values)
    print("Standard scaling for comparison:\n", StandardScaler().fit(train).transform(query))
    if hasattr(scaler, "center_"):
        print("Median / IQR:", scaler.center_, scaler.scale_)
else:
    print("Fit a median-and-IQR scaler without removing observations.")
