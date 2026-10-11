import numpy as np

def weighted_score(scores, weights):
    """Return the 1D dot product."""
    return np.dot(scores, weights)

print(weighted_score(np.array([5, 2, 4]), np.array([2, 3, 1])))
