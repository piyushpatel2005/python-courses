from solution import *
import numpy as np

def test_view_and_copy():
    """The view shares memory and the snapshot does not"""
    for values in ([2, 4, 6, 8], [9, 11, 13, 15]):
        original = np.array(values)
        view, snapshot = calibrate(original)
        assert np.shares_memory(original, view)
        assert not np.shares_memory(original, snapshot)
        assert np.array_equal(original, [values[0], 50, values[2], values[3]])
        assert np.array_equal(view, [50, values[2]])
        assert np.array_equal(snapshot, [-5, values[2]])
