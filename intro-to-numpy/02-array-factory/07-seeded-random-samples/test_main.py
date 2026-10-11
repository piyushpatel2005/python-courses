from solution import *
import numpy as np

def test_upper_bound():
    """Integer samples use the new upper bound"""
    assert np.array_equal(first, np.random.default_rng(21).integers(0, 10, size=4))
    assert np.array_equal(again, first)
