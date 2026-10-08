from solution import *
import numpy as np

def test_seeded_feeds():
    """All three feeds replay from a fresh generator"""
    for seed, count in [(42, 3), (8, 5)]:
        rng = np.random.default_rng(seed)
        expected = (rng.integers(0, 10, size=count), rng.uniform(0, 1, size=count), rng.normal(0, 1, size=count))
        result = simulate_feeds(seed, count)
        assert len(result) == 3
        for actual, target in zip(result, expected):
            assert isinstance(actual, np.ndarray) and np.array_equal(actual, target)
