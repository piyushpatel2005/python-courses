import numpy as np
from sklearn.datasets import make_regression, make_classification


def generate(seed, n_rows):
    # Return the result described in the task.
    return None


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
