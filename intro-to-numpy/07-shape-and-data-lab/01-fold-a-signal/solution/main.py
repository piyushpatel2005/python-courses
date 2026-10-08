import numpy as np

signal = np.array([4, 7, 2, 8, 5, 9])
card = signal.reshape(3, 2)
flat = card.ravel()
print("card shape:", card.shape, "size:", card.size)
print("unrolled:", flat)
