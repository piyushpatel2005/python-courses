import numpy as np
from solution import *


def test_turn_the_grid():
    assert turned.shape == (grid.shape[1], grid.shape[0]) and np.array_equal(turned, grid.T)
