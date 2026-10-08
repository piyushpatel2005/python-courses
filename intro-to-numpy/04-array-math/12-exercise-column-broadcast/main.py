import numpy as np

def row_correction(grid, baselines):
    # Convert baselines to a column and subtract from grid.
    return None

def incompatible(grid, offsets):
    # Return True if grid + offsets raises ValueError, else False.
    return None

print(row_correction(np.array([[5, 9], [8, 4]]), np.array([1, 3])))
print(incompatible(np.ones((2, 3)), np.array([1, 2, 3, 4])))
