import numpy as np

def hold_settings(settings, frames):
    return np.repeat(settings, frames)

def cycle_settings(settings, cycles):
    return np.tile(settings, cycles)

settings = np.array([1, 4, 7])
print("held:", hold_settings(settings, 2))
print("cycle:", cycle_settings(settings, 2))
