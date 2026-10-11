import numpy as np

def ordered_nights(grid):
    """Return each row sorted without changing the input."""
    return np.sort(grid, axis=1)

print(ordered_nights(np.array([[7, 2, 5], [6, 9, 1]])))
