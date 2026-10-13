import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC


def select_rbf(training, labels, validation, actual, candidates):
    return None

records = pd.read_csv("classification-measurements.csv", float_precision="round_trip")
X = records[['feature_1', 'feature_2']]
y = records["class_label"]
training, validation, labels, actual = train_test_split(X, y, test_size=0.3, random_state=29, stratify=y)
candidates = [(1., 0.2), (8., 2.)]

print("Selected C/gamma and validation scores:", select_rbf(training, labels, validation, actual, candidates))
