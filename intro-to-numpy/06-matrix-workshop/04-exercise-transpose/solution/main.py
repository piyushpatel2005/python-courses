import numpy as np

def rounds_first(scores):
    """Return the transposed scoreboard."""
    return scores.T

print(rounds_first(np.array([[2, 5, 8], [4, 7, 1]])))
