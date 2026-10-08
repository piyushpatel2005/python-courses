import numpy as np

def row_correction(grid, baselines):
    return grid - baselines[:, np.newaxis]

def incompatible(grid, offsets):
    try:
        grid + offsets
    except ValueError:
        return True
    return False

print(row_correction(np.array([[5, 9], [8, 4]]), np.array([1, 3])))
print(incompatible(np.ones((2, 3)), np.array([1, 2, 3, 4])))
