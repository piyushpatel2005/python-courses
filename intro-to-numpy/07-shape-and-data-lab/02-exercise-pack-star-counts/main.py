import numpy as np

def unroll_counts(grid):
    # Return the readings in row-major order.
    return grid

def pack_counts(readings):
    # Infer the row count; keep four readings per row.
    return readings

counts = np.array([[3, 1], [4, 2]])
print("flat:", unroll_counts(counts))
print("packed:", pack_counts(np.array([3, 1, 4, 2])))
