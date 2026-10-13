import pandas as pd
import numpy as np
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import Lasso
from sklearn.metrics import mean_absolute_error


def fit_lasso(training, target, alpha):
    return Pipeline([("scale", StandardScaler()), ("lasso", Lasso(alpha=alpha, max_iter=5000, tol=1e-6))]).fit(training, target)

records = pd.read_csv("regression-measurements.csv", float_precision="round_trip")
X = records[['feature_1', 'feature_2', 'feature_3', 'feature_4', 'feature_5']]
y = records["target_value"]
training, target = X[:70], y[:70]
validation, actual = X[70:], y[70:]

model = fit_lasso(training, target, 2.)
if model is not None:
    print("Scaled coefficients:", model.named_steps["lasso"].coef_)
    print("Validation MAE:", mean_absolute_error(actual, model.predict(validation)))
else:
    print("Fit the Lasso pipeline.")
