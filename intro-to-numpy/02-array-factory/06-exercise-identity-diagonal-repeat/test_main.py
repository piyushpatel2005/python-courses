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

def test_identity():
    """Identity grid has diagonal ones"""
    for count in (2, 4):
        assert np.array_equal(_constructed(station_identity, (count,), "eye"), np.eye(count))

def test_weights():
    """Weights appear only on the diagonal"""
    for values in ([3, 1], [2, 4, 6]):
        assert np.array_equal(_constructed(station_weights, (values,), "diag"), np.diag(values))

def test_repeat():
    """A signal repeats the requested number of times"""
    assert np.array_equal(_constructed(hold_signal, (7, 3), "repeat"), [7, 7, 7])
    assert np.array_equal(_constructed(hold_signal, (2, 2), "repeat"), [2, 2])
