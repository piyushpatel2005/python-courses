from solution import *
import numpy as np

def test_identity():
    """Identity grid has diagonal ones"""
    for count in (2, 4):
        assert np.array_equal(station_identity(count), np.eye(count))

def test_weights():
    """Weights appear only on the diagonal"""
    for values in ([3, 1], [2, 4, 6]):
        assert np.array_equal(station_weights(values), np.diag(values))

def test_repeat():
    """A signal repeats the requested number of times"""
    assert np.array_equal(hold_signal(7, 3), [7, 7, 7])
    assert np.array_equal(hold_signal(2, 2), [2, 2])
