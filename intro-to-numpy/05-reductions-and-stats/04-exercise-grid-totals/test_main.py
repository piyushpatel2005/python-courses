import numpy as np
from solution import *


def test_exercise_grid_totals():
    for values in ([[4, 8, 2], [6, 3, 7]], [[2, 7], [8, 1], [4, 6]]):
        a = np.array(values)
        columns, rows = totals(a)
        assert np.array_equal(columns, np.sum(a, axis=0))
        assert np.array_equal(rows, np.sum(a, axis=1))
