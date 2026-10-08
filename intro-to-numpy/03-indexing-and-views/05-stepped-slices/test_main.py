from solution import *
import numpy as np

def test_slice_assignment():
    """Replace odd-indexed samples"""
    assert np.array_equal(pulses, [10, -1, 12, -1, 14, -1])
