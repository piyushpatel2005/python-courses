import numpy as np

readings = np.array([2, 4, 6])
weights = np.array([3, 1, 2])
weighted = np.dot(readings, weights)
print(weighted)
