import numpy as np

def calibrate_pressure(raw, gain, offset):
    # Multiply every raw value by gain, then add offset.
    return None

print(calibrate_pressure(np.array([2, 4, 6]), 3, 1))
