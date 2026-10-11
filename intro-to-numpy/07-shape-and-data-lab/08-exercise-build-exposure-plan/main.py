import numpy as np

def hold_settings(settings, frames):
    return settings

def cycle_settings(settings, cycles):
    return settings

settings = np.array([1, 4, 7])
print("held:", hold_settings(settings, 2))
print("cycle:", cycle_settings(settings, 2))
