import numpy as np

def panel_basics(grid):
    night_totals = np.sum(grid, axis=1)
    sensor_means = np.mean(grid, axis=0)
    return night_totals, sensor_means

def panel_variability(grid):
    night_medians = np.median(grid, axis=1)
    sensor_std = np.std(grid, axis=0)
    return night_medians, sensor_std

panel = np.array([[4, 6, 2], [8, 3, 7]])
print("totals and means:", panel_basics(panel))
print("medians and spread:", panel_variability(panel))
