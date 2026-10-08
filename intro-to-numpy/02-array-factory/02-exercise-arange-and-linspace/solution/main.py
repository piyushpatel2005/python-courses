import numpy as np

def sample_times(start, stop, step):
    return np.arange(start, stop, step)

def calibration_marks(start, stop, count):
    return np.linspace(start, stop, count)

print(sample_times(1, 8, 2))
print(calibration_marks(0, 2, 3))
