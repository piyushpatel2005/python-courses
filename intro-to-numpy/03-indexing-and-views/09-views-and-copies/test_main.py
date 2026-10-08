from solution import *
import numpy as np

def test_view_copy():
    """A slice edit reaches the source, but a copy edit does not"""
    assert np.array_equal(record, [6, 70, 8, 9])
    assert np.shares_memory(record, window)
    assert not np.shares_memory(record, backup)
