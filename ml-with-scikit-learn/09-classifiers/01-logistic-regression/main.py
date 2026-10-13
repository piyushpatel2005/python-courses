import numpy as np
from sklearn.datasets import load_iris, load_wine
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression


def fit_classifier(training, labels, C):
    return Pipeline([("scale", StandardScaler()), ("model", LogisticRegression(C=1.0, max_iter=1000, n_jobs=1, random_state=17))]).fit(training, labels)

data = load_iris()
training, queries, labels, actual = train_test_split(data.data, data.target, test_size=0.25, random_state=17, stratify=data.target)

model = fit_classifier(training, labels, 0.2)
if model is not None:
    print("Class order:", model.classes_)
    print("Labels:", model.predict(queries[:3]))
    print("Probabilities:", model.predict_proba(queries[:3]))
else:
    print("Fit the classifier.")
