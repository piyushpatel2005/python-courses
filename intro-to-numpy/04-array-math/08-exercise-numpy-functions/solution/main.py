import numpy as np

def transform(angles, intensities):
    return np.sin(angles), np.log(intensities)

print(transform(np.array([0.0, np.pi / 2]), np.array([1.0, np.e])))
