import numpy as np

def describe(readings):
    mean = np.mean(readings)
    median = np.median(readings)
    variance = np.var(readings)
    std = np.std(readings)
    return mean, median, variance, std

print(describe(np.array([40., 44., 48.])))
