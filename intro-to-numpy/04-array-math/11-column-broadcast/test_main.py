from solution import *
import numpy as np

def test_column_broadcast():
    """Subtract a separate baseline from each row"""
    assert np.array_equal(corrected, [[1, 3], [4, 6], [7, 9]])
