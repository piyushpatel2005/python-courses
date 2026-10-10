import numpy as np

def transform_panel(grid, calibration):
    """Return 2D matrix multiplication."""
    return grid @ calibration

def calibrated_channels(grid, calibration):
    """Return calibrated measurements with channels in rows."""
    return transform_panel(grid, calibration).T

def channel_peaks(grid, calibration):
    """Return maximum calibrated reading for each output channel."""
    return None

panel = np.array([[2, 4], [5, 1]])
calibration = np.array([[1, 2, 0], [0, 1, 3]])
print("calibrated channels:", calibrated_channels(panel, calibration))
print("channel peaks:", channel_peaks(panel, calibration))
