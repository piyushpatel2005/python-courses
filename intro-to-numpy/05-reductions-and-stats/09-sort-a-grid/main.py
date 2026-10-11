import numpy as np

samples = np.array([[8, 3, 6], [4, 9, 1]])
by_microphone = np.sort(samples, axis=0)
print(by_microphone)
