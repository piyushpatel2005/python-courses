import numpy as np

def simulate_feeds(seed, count):
    rng = np.random.default_rng(seed)
    counts = rng.integers(0, 10, size=count)
    fractions = rng.uniform(0, 1, size=count)
    noise = rng.normal(0, 1, size=count)
    return counts, fractions, noise

print(simulate_feeds(42, 3))
