import numpy as np


def make_xy(records):
    X = records[:, :1].copy()
    y = records[:, 2].copy()
    return X, y


# Supplied fixture and observation probe.
records = np.array([[1., 4., 5.], [2., 7., 7.], [3., 8., 9.], [4., 12., 11.]])

result = make_xy(records)
if result is not None:
    X, y = result
    print("X shape:", X.shape, "y shape:", y.shape)
    print("First paired row:", X[0], y[0])
else:
    print("Build the aligned feature and target arrays.")
