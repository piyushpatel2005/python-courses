import numpy as np
from solution import *


def test_exercise_transpose():
    for values in ([[2, 5, 8], [4, 7, 1]], [[1, 4], [7, 2], [5, 9]]):
        a = np.array(values)
        assert np.array_equal(rounds_first(a), a.T)
        assert rounds_first(a).shape == (a.shape[1], a.shape[0])
