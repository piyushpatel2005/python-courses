import numpy as np

def locate(grid):
    return grid[:, 1], grid[-1, -1]

print(locate(np.array([[2, 6, 4], [7, 5, 8]])))
