import numpy as np

def remove_background(grid, offsets):
    return grid - offsets

print(remove_background(np.array([[11, 22], [13, 26]]), np.array([1, 2])))
