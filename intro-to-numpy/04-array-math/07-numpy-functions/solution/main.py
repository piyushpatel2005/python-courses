import numpy as np
angles = np.array([0.0, np.pi / 2])
wave = np.sin(angles)
print(np.round(wave, 3))
positive = np.array([1.0, np.e])
print(np.round(np.log(positive), 3))
print(np.round(np.exp(np.array([0.0, 1.0])), 3))
