from solution import *
import numpy as np

def test_mask():
    """Replace all readings over 20"""
    assert np.array_equal(readings, [8, 0, 16, 0])
