import numpy as np
from solution import *


def test_multiply_matrices():
    assert combined.shape == (grid.shape[0], calibration.shape[1]) and np.array_equal(combined, np.matmul(grid, calibration))
