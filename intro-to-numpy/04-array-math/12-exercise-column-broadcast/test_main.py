from solution import *
import numpy as np

def test_row_correction():
    """Subtract one baseline from each entire row"""
    assert np.array_equal(row_correction(np.array([[5, 9], [8, 4]]), np.array([1, 3])), [[4, 8], [5, 1]])
    assert np.array_equal(row_correction(np.array([[7, 8, 9], [4, 5, 6]]), np.array([2, 4])), [[5, 6, 7], [0, 1, 2]])

def test_incompatible():
    """Catch only incompatible broadcasting shapes"""
    assert incompatible(np.ones((2, 3)), np.array([1, 2, 3, 4])) is True
    assert incompatible(np.ones((2, 3)), np.array([1, 2, 3])) is False
