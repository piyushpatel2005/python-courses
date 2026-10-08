import numpy as np

def panel_basics(grid):
    """Return (night totals, sensor means) from the previous step."""
    return np.sum(grid, axis=1), np.mean(grid, axis=0)

def panel_variability(grid):
    """Return (night medians, sensor population std)."""
    return None

panel = np.array([[4, 6, 2], [8, 3, 7]])
print("totals and means:", panel_basics(panel))
print("medians and spread:", panel_variability(panel))
