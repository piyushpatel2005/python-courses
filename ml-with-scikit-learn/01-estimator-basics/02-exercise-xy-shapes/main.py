import numpy as np


def make_xy(records):
    # Return the result described in the task.
    return None


# Supplied fixture and observation probe.
records = np.array([[12., 20., 35.], [18., 30., 48.], [24., 45., 67.], [30., 50., 80.], [36., 65., 96.]])

result = make_xy(records)
if result is not None:
    X, y = result
    print("X shape:", X.shape, "y shape:", y.shape)
    print("First paired row:", X[0], y[0])
else:
    print("Build the aligned feature and target arrays.")
