import numpy as np
from solution import *


def test_exercise_sort_grid():
    for values in ([[7, 2, 5], [6, 9, 1]], [[8, 2], [4, 3], [1, 7]]):
        a = np.array(values)
        original = a.copy()
        assert np.array_equal(ordered_nights(a), np.sort(a, axis=1))
        assert np.array_equal(a, original)
