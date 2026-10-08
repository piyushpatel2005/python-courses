import numpy as np
from solution import *


def test_exercise_select_sensor():
    for values, col in [([[4, 1], [7, 6], [3, 8]], 1), ([[9, 3, 2], [6, 7, 5]], 0)]:
        a = np.array(values)
        assert np.array_equal(sensor_history(a, col), a[:, col])
