import numpy as np
from sklearn.dummy import DummyRegressor, DummyClassifier
from sklearn.metrics import mean_absolute_error, accuracy_score
import pandas as pd


def baseline(X_train, y_train, X_valid, y_valid):
    # Return the result described in the task.
    return None


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
