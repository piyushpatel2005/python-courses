import numpy as np
first = np.random.default_rng(21).integers(0, 10, size=4)
again = np.random.default_rng(21).integers(0, 10, size=4)
print(first.tolist(), np.array_equal(first, again))
effects = np.random.default_rng(7)
fractions = effects.uniform(0, 1, size=3)
noise = effects.normal(0, 1, size=3)
print(fractions.round(2).tolist(), noise.round(2).tolist())
