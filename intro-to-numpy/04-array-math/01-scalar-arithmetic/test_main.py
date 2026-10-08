from solution import *
import numpy as np

def test_offset():
    """Double each reading then add four"""
    assert np.array_equal(corrected, [10, 14, 18])
