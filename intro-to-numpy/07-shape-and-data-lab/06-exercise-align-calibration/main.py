import numpy as np

def as_column(offsets):
    return offsets

def as_row(ticks):
    return ticks

print("offsets:", as_column(np.array([1, 3, 5, 7])).shape)
print("ticks:", as_row(np.array([0, 10, 20])).shape)
