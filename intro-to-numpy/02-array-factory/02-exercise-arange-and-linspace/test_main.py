from solution import *
import numpy as np

def _constructed(function, args, name):
    original = getattr(np, name)
    calls = []
    def traced(*args, **kwargs):
        calls.append(True)
        return original(*args, **kwargs)
    setattr(np, name, traced)
    try:
        result = function(*args)
    finally:
        setattr(np, name, original)
    assert calls, "Use np." + name + " for this pattern"
    assert isinstance(result, np.ndarray), "Return a NumPy array"
    return result

def test_sample_times():
    """Stepped times exclude the stop"""
    for args in [(1, 8, 2), (0, 5, 2), (6, 0, -2), (4, 4, 1)]:
        actual = _constructed(sample_times, args, "arange")
        assert isinstance(actual, np.ndarray), "Return a NumPy array"
        assert np.array_equal(actual, np.arange(*args))

def test_calibration_marks():
    """Calibration marks include both ends"""
    for args in [(0, 2, 3), (1, 3, 5), (-1, 1, 7), (2, 2, 4)]:
        actual = _constructed(calibration_marks, args, "linspace")
        assert isinstance(actual, np.ndarray), "Return a NumPy array"
        assert actual.shape == (args[2],), "Return exactly count points"
        assert np.allclose(actual, np.linspace(*args), rtol=1e-7, atol=1e-9)
        assert np.isclose(actual[0], args[0]) and np.isclose(actual[-1], args[1])
