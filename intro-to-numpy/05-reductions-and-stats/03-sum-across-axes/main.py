import numpy as np

grid = np.array([[2, 5, 3], [4, 1, 6]])
night_totals = np.sum(grid, axis=0)
print(night_totals)
