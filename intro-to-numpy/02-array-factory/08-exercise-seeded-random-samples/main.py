import numpy as np

def simulate_feeds(seed, count):
    rng = np.random.default_rng(seed)
    counts = None
    fractions = None
    noise = None
    return counts, fractions, noise

print(simulate_feeds(42, 3))
