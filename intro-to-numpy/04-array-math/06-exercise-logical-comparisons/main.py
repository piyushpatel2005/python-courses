import numpy as np

def in_window(readings, low, high):
    # Return a boolean mask for low <= reading <= high.
    return None

def matches_window(readings, expected, low, high):
    # Compare the computed mask with expected using np.array_equal.
    return None

print(in_window(np.array([1, 4, 7, 10]), 4, 7))
print(matches_window(np.array([1, 4, 7, 10]), np.array([False, True, True, False]), 4, 7))
