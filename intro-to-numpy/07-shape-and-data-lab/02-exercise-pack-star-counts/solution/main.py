import numpy as np

def unroll_counts(grid):
    return grid.ravel()

def pack_counts(readings):
    return readings.reshape(-1, 4)

counts = np.array([[3, 1], [4, 2]])
print("flat:", unroll_counts(counts))
print("packed:", pack_counts(np.array([3, 1, 4, 2])))
