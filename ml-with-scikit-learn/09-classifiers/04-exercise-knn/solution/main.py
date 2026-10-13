import numpy as np
from sklearn.datasets import load_iris, load_wine
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier


def fit_neighbors(training, labels, k):
    return Pipeline([("scale", StandardScaler()), ("model", KNeighborsClassifier(n_neighbors=k, n_jobs=1))]).fit(training, labels)

data = load_wine()
training, queries, labels, actual = train_test_split(data.data[:, [0, 6]], data.target, test_size=0.25, random_state=29, stratify=data.target)

model = fit_neighbors(training, labels, 3)
print("Neighbor predictions:", None if model is None else model.predict(queries[:5]))
