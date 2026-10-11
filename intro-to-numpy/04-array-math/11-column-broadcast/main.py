import numpy as np
grid = np.array([[2, 4], [6, 8], [10, 12]])
baselines = np.array([1, 2, 3])
column = baselines[:, np.newaxis]
corrected = grid + column  # Change + to -.
print(column.shape, corrected)
try:
    grid + np.array([1, 2, 3, 4])
except ValueError:
    print('Incompatible shapes')
