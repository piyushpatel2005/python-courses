import numpy as np
from sklearn.datasets import load_iris, load_wine


def select_bundle(bundle, rows):
    X = bundle.data[rows]
    y = bundle.target[:len(rows)]
    return X, y, list(bundle.feature_names), list(bundle.target_names)


# Supplied fixture and observation probe.
bundle = load_iris()
rows = np.array([0, 50, 100, 149])

result = select_bundle(bundle, rows)
if result is not None:
    X, y, names, classes = result
    print("Shapes:", X.shape, y.shape)
    print("Feature names:", names)
    print("Targets:", y, "class names:", classes)
else:
    print("Select aligned benchmark rows and retain their names.")
