import numpy as np

raw = np.arange(6)
card = raw.reshape(2, 3)  # Change the shape.
shared = np.shares_memory(raw, card)
print("card:", card.shape, "shares storage:", shared)
