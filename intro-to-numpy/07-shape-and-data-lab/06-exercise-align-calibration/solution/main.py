import numpy as np

def as_column(offsets):
    return offsets[:, np.newaxis]

def as_row(ticks):
    return ticks[np.newaxis, :]

print("offsets:", as_column(np.array([1, 3, 5, 7])).shape)
print("ticks:", as_row(np.array([0, 10, 20])).shape)
