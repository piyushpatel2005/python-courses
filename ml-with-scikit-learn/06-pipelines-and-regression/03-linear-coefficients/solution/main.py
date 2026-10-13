import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression


def reconstruct(model, queries):
    return model.intercept_ + queries @ model.coef_

records = pd.read_csv("regression-measurements.csv", float_precision="round_trip")
X = records[['feature_1', 'feature_2']]
y = records["target_value"]
model = LinearRegression(n_jobs=1).fit(X[:60], y[:60])
queries = X[60:63]

print("Reconstructed:", reconstruct(model, queries))
print("Estimator predictions:", model.predict(queries))
