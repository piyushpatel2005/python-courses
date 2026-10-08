import numpy as np

def extremes(readings):
    """Return (sum, minimum, maximum, index of min, index of max)."""
    return (np.sum(readings), np.min(readings), np.max(readings), np.argmin(readings), np.argmax(readings))

print(extremes(np.array([9, 3, 14, 6])))
