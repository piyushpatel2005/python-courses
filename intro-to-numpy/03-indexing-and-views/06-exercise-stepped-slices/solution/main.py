import numpy as np

def mute_interior(readings):
    updated = readings.copy()
    updated[1:-1:2] = -9
    return updated

print(mute_interior(np.array([3, 4, 5, 6, 7])))
