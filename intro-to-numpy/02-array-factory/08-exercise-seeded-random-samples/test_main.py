from solution import *
import numpy as np

def _expected(seed, count):
    rng = np.random.default_rng(seed)
    return (rng.integers(0, 10, size=count),
            rng.uniform(0, 1, size=count),
            rng.normal(0, 1, size=count))

def _check_feed(index):
    for seed, count in [(42, 3), (8, 5), (0, 1), (19, 0)]:
        actual = simulate_feeds(seed, count)[index]
        target = _expected(seed, count)[index]
        assert isinstance(actual, np.ndarray), "Return a NumPy array in this feed's slot"
        assert actual.shape == (count,), "Use size=count"
        if index == 0:
            assert actual.dtype.kind in 'iu' and np.array_equal(actual, target)
        else:
            assert actual.dtype.kind == 'f'
            assert np.allclose(actual, target, rtol=1e-7, atol=1e-9)
        assert np.array_equal(actual, simulate_feeds(seed, count)[index]), "Restart with the supplied seed on each call"

def test_integer_feed():
    """Draw integer counts from the seeded generator"""
    _check_feed(0)

def test_uniform_feed():
    """Draw uniform fractions after the integer draw"""
    _check_feed(1)

def test_normal_feed():
    """Draw normal noise after the uniform draw"""
    _check_feed(2)
