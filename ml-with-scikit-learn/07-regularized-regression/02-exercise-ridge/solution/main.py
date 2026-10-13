import pandas as pd
import numpy as np
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import Ridge
from sklearn.metrics import mean_absolute_error


def fit_ridge(training, target, alpha):
    return Pipeline([("scale", StandardScaler()), ("ridge", Ridge(alpha=alpha))]).fit(training, target)

records = pd.read_csv("regression-measurements.csv", float_precision="round_trip")
X = records[['feature_1', 'feature_2', 'feature_3', 'feature_4']]
y = records["target_value"]
training, target = X[:70], y[:70]
validation, actual = X[70:], y[70:]

for alpha in (0.1, 10.):
    model = fit_ridge(training, target, alpha)
    print("alpha / validation MAE:", alpha, None if model is None else mean_absolute_error(actual, model.predict(validation)))
