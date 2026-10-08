import numpy as np

def describe(readings):
    """Return (mean, median, population variance, population std)."""
    return np.mean(readings), np.median(readings), np.var(readings), np.std(readings)

print(describe(np.array([40., 44., 48.])))
