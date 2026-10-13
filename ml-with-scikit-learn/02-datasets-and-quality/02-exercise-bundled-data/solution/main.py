import numpy as np
from sklearn.datasets import load_iris, load_wine


def select_bundle(bundle, rows):
    X = bundle.data[rows]
    y = bundle.target[rows]
    return X, y, list(bundle.feature_names), list(bundle.target_names)


# Supplied fixture and observation probe.
bundle = load_wine()
rows = np.array([4, 75, 135, 170, 22])

result = select_bundle(bundle, rows)
if result is not None:
    X, y, names, classes = result
    print("Shapes:", X.shape, y.shape)
    print("Feature names:", names)
    print("Targets:", y, "class names:", classes)
else:
    print("Select aligned benchmark rows and retain their names.")
