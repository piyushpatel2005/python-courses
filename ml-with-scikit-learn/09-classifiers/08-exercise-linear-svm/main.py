import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.svm import LinearSVC


def fit_margin(training, labels, C):
    return None

records = pd.read_csv("classification-measurements.csv", float_precision="round_trip")
X = records[['feature_1', 'feature_2', 'feature_3']]
y = records["class_label"]
training, queries, labels, actual = train_test_split(X, y, test_size=0.3, random_state=29, stratify=y)

model = fit_margin(training, labels, 0.2)
if model is not None:
    print("Signed scores:", model.decision_function(queries[:4]))
    print("Predicted classes:", model.predict(queries[:4]))
else:
    print("Fit the margin classifier.")
