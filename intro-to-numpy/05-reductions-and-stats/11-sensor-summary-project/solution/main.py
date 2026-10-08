import numpy as np

def panel_basics(grid):
    """Return (night totals, sensor means)."""
    return np.sum(grid, axis=1), np.mean(grid, axis=0)

print(panel_basics(np.array([[4, 6, 2], [8, 3, 7]])))
