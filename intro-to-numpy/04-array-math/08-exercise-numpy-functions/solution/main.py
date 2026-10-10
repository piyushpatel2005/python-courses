import numpy as np

def transform(angles, intensities):
    sine_values = np.sin(angles)
    log_values = np.log(intensities)
    return sine_values, log_values

print(transform(np.array([np.pi / 6, -np.pi / 2]), np.array([np.e ** 2, np.e ** 3])))
