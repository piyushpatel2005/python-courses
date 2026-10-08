import numpy as np

def calibrate(record):
    # Take a view of the middle two elements and a separate copy.
    # Set the view first element to 50, then the copy first element to -5.
    # Return (view, snapshot).
    return None

sample = np.array([2, 4, 6, 8])
print(calibrate(sample), sample)
