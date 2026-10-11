import numpy as np

def locate(grid):
    column = grid[:, 1]
    corner = grid[-1, -1]
    return column, corner

print(locate(np.array([[2, 6, 4], [7, 5, 8]])))
