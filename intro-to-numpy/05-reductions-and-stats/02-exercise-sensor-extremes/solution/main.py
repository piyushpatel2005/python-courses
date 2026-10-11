import numpy as np

def extremes(readings):
    total = np.sum(readings)
    minimum = np.min(readings)
    maximum = np.max(readings)
    min_index = np.argmin(readings)
    max_index = np.argmax(readings)
    return total, minimum, maximum, min_index, max_index

print(extremes(np.array([9, 3, 14, 6])))
