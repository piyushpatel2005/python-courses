import numpy as np

signal = np.array([4, 7, 2, 8, 5, 9])
card = signal.reshape(2, 3)  # Change just these dimensions.
flat = card.ravel()
print("card shape:", card.shape, "size:", card.size)
print("unrolled:", flat)
