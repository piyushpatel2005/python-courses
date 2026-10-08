import numpy as np

grid = np.array([[1, 2, 3], [4, 5, 6]])
calibration = np.array([[1, 0], [0, 1], [1, 1]])
combined = grid @ calibration
print(combined)
