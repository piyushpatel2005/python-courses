import numpy as np
from sklearn.datasets import make_regression, make_classification


def generate(seed, n_rows):
    return make_classification(n_samples=n_rows, n_features=3, n_informative=2, n_redundant=0, n_classes=2, random_state=seed)


# Supplied fixture and observation probe.
seed = 29
n_rows = 100

result = generate(seed, n_rows)
if result is not None:
    X, y = result
    print("Shapes:", X.shape, y.shape)
    print("First two targets:", y[:2])
else:
    print("Generate the requested synthetic fixture.")
