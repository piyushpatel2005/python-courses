import numpy as np

raw = np.arange(6)
card = raw.reshape(3, 2)
shared = np.shares_memory(raw, card)
print("card:", card.shape, "shares storage:", shared)
