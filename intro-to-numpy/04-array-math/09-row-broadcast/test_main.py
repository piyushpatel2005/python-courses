from solution import *
import numpy as np

def test_broadcast_rows():
    """Subtract the same vector from both rows"""
    assert np.array_equal(adjusted, [[-9, -18, -27], [-6, -15, -24]])
