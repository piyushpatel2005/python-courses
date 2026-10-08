import numpy as np
from solution import *


def test_exercise_transform_grid():
    for a, b in [([[2, 3, 5], [7, 1, 4]], [[1, 2], [0, 1], [2, 0]]), ([[3, 8], [4, 1], [5, 7]], [[2, 1, 0], [1, 0, 3]])]:
        left, right = np.array(a), np.array(b)
        assert np.array_equal(transform_panel(left, right), left @ right)
        assert transform_panel(left, right).shape == (left.shape[0], right.shape[1])
