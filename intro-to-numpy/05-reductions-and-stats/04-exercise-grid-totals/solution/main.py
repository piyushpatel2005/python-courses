import numpy as np

def totals(scores):
    """Return (total per round, total per player)."""
    return np.sum(scores, axis=0), np.sum(scores, axis=1)

print(totals(np.array([[4, 8, 2], [6, 3, 7]])))
