import numpy as np

def panel_basics(grid):
    night_totals = np.sum(grid, axis=1)
    sensor_means = np.mean(grid, axis=0)
    return night_totals, sensor_means

print(panel_basics(np.array([[4, 6, 2], [8, 3, 7]])))
