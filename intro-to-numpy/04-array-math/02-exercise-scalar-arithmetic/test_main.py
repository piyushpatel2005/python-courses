from solution import *
import numpy as np

def test_calibrate():
    """Apply both supplied scalars elementwise"""
    assert np.array_equal(calibrate_pressure(np.array([2, 4, 6]), 3, 1), [7, 13, 19])
    assert np.array_equal(calibrate_pressure(np.array([1, 5]), 2, -3), [-1, 7])
