import numpy as np
from sklearn.datasets import make_regression, make_classification


def generate(seed, n_rows):
    return make_regression(n_samples=n_rows, n_features=2, n_informative=2, noise=3.0, random_state=17)


# Supplied fixture and observation probe.
seed = 29
n_rows = 80

result = generate(seed, n_rows)
if result is not None:
    X, y = result
    print("Shapes:", X.shape, y.shape)
    print("First two targets:", y[:2])
else:
    print("Generate the requested synthetic fixture.")
