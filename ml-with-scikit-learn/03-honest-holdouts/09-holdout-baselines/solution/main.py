import numpy as np
from sklearn.dummy import DummyRegressor, DummyClassifier
from sklearn.metrics import mean_absolute_error, accuracy_score
import pandas as pd


def baseline(X_train, y_train, X_valid, y_valid):
    model = DummyRegressor(strategy="mean").fit(X_train, y_train)
    predictions = model.predict(X_valid)
    return model, mean_absolute_error(y_valid, predictions)


# Supplied fixture and observation probe.
training = pd.read_csv("training.csv")
validation = pd.read_csv("validation.csv")
X_train = training[["feature_0"]].to_numpy()
y_train = training["target"].to_numpy()
X_valid = validation[["feature_0"]].to_numpy()
y_valid = validation["target"].to_numpy()

result = baseline(X_train, y_train, X_valid, y_valid)
if result is not None:
    model, metric = result
    print("Validation metric:", metric)
    print("First predictions:", model.predict(X_valid[:3]))
else:
    print("Fit a training-only dummy baseline and evaluate validation rows.")
