import numpy as np

def describe(readings):
    mean = None
    median = None
    variance = None
    std = None
    return mean, median, variance, std

print(describe(np.array([40., 44., 48.])))
