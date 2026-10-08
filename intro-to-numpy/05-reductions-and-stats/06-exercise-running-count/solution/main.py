import numpy as np

def running_count(counts):
    """Return cumulative counts, in original order."""
    return np.cumsum(counts)

print(running_count(np.array([2, 5, 1])))
