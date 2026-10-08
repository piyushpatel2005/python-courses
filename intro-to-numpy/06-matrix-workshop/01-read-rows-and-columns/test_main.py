import numpy as np
from solution import *


def test_read_rows_and_columns():
    assert np.array_equal(sensor_history, grid[:, 1]) and sensor_history.shape == (grid.shape[0],)
