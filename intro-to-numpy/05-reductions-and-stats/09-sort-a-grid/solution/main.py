import numpy as np

samples = np.array([[8, 3, 6], [4, 9, 1]])
by_microphone = np.sort(samples, axis=1)
print(by_microphone)
