from solution import *
import numpy as np

def test_window():
    """Return a boolean mask with inclusive bounds"""
    assert np.array_equal(in_window(np.array([1, 4, 7, 10]), 4, 7), [False, True, True, False])
    assert np.array_equal(in_window(np.array([8, 3, 6]), 5, 8), [True, False, True])

def test_matches_window():
    """Compare the entire boolean array and its shape"""
    readings = np.array([1, 4, 7, 10])
    assert matches_window(readings, np.array([False, True, True, False]), 4, 7) is True
    assert matches_window(readings, np.array([False, True, False, False]), 4, 7) is False
    assert matches_window(readings, np.array([[False, True, True, False]]), 4, 7) is False
    assert matches_window(np.array([8, 3, 6]), np.array([True, False, True]), 5, 8) is True
