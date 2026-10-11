from solution import *
import numpy as np

def test_calibrate():
    """Apply both supplied scalars elementwise"""
    assert np.array_equal(calibrate_pressure(np.array([2, 4, 6]), 3, 1), [7, 13, 19])
    assert np.array_equal(calibrate_pressure(np.array([1, 5]), 2, -3), [-1, 7])
    original = np.array([2., -4., 8.])
    raw = original.copy()
    result = calibrate_pressure(raw, 0.5, -2)
    assert isinstance(result, np.ndarray), "Return a NumPy array."
    assert np.array_equal(raw, original), "Leave raw unchanged."
    assert not np.shares_memory(raw, result), "Return a new array."
    assert np.allclose(result, [-1., -4., 2.])
