from solution import *
import numpy as np

def test_difference():
    """Subtract arrays position by position"""
    assert np.array_equal(difference(np.array([9, 4, 8]), np.array([3, 2, 5])), [6, 2, 3])
    assert np.array_equal(difference(np.array([12, 1]), np.array([5, 7])), [7, -6])
