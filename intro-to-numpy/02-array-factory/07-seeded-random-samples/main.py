import numpy as np
# The same seed replays the same score draws. Change the upper bound to 10.
first = np.random.default_rng(21).integers(0, 6, size=4)
again = np.random.default_rng(21).integers(0, 6, size=4)
print(first.tolist(), np.array_equal(first, again))
effects = np.random.default_rng(7)
fractions = effects.uniform(0, 1, size=3)
noise = effects.normal(0, 1, size=3)
print(fractions.round(2).tolist(), noise.round(2).tolist())
