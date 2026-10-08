from solution import *
import numpy as np

def test_locate():
    """Select column and corner by coordinates"""
    col, corner = locate(np.array([[2, 6, 4], [7, 5, 8]]))
    assert np.array_equal(col, [6, 5]) and corner == 8
    col, corner = locate(np.array([[9, 1, 2], [3, 4, 5], [6, 8, 7]]))
    assert np.array_equal(col, [1, 4, 8]) and corner == 7
