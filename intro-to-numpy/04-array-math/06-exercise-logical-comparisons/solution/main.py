import numpy as np

def in_window(readings, low, high):
    return (readings >= low) & (readings <= high)

def matches_window(readings, expected, low, high):
    return bool(np.array_equal(in_window(readings, low, high), expected))

print(in_window(np.array([1, 4, 7, 10]), 4, 7))
print(matches_window(np.array([1, 4, 7, 10]), np.array([False, True, True, False]), 4, 7))
