import numpy as np

def extremes(readings):
    total = None
    minimum = None
    maximum = None
    min_index = None
    max_index = None
    return total, minimum, maximum, min_index, max_index

print(extremes(np.array([9, 3, 14, 6])))
