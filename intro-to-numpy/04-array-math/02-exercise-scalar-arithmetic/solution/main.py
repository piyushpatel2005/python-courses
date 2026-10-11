import numpy as np

def calibrate_pressure(raw, gain, offset):
    return raw * gain + offset

print(calibrate_pressure(np.array([2, 4, 6]), 3, 1))
