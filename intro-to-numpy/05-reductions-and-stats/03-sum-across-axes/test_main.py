import numpy as np
from solution import *


def test_sum_across_axes():
    assert np.array_equal(night_totals, np.sum(grid, axis=1)) and night_totals.shape == (grid.shape[0],)
