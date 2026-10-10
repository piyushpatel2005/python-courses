from solution import *
import numpy as np

def test_row_broadcast():
    """Apply one offset per column to every row"""
    assert np.array_equal(remove_background(np.array([[11, 22], [13, 26]]), np.array([1, 2])), [[10, 20], [12, 24]])
    assert np.array_equal(remove_background(np.array([[3, 7, 9], [8, 10, 12]]), np.array([2, 1, 4])), [[1, 6, 5], [6, 9, 8]])
