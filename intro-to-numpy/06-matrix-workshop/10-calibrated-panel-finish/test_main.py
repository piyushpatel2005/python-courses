import numpy as np
from solution import *


def test_calibrated_panel_finish():
    for a, b in [([[2, 4], [5, 1]], [[1, 2, 0], [0, 1, 3]]), ([[3, 7], [8, 2], [1, 5]], [[2, 0, 1], [1, 3, 0]])]:
        left, right = np.array(a), np.array(b)
        assert np.array_equal(channel_peaks(left, right), np.max(left @ right, axis=0))
