import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression


def reconstruct(model, queries):
    return None

records = pd.read_csv("regression-measurements.csv", float_precision="round_trip")
dimensions = records[['feature_1', 'feature_2', 'feature_3']]
prices = records["target_value"]
model = LinearRegression(n_jobs=1).fit(dimensions[:65], prices[:65])
queries = dimensions[65:69]

print("Reconstructed:", reconstruct(model, queries))
print("Estimator predictions:", model.predict(queries))
