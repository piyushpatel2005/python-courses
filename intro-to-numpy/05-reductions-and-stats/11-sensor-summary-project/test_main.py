import numpy as np
from solution import *


def test_sensor_summary_project():
    for values in ([[4, 6, 2], [8, 3, 7]], [[3, 1], [5, 9], [7, 2]]):
        a = np.array(values)
        nights, sensors = panel_basics(a)
        assert np.array_equal(nights, np.sum(a, axis=1))
        assert np.allclose(sensors, np.mean(a, axis=0))
