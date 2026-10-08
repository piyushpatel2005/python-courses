import numpy as np
from solution import *


def test_sensor_summary_finish():
    for values in ([[4, 6, 20], [8, 3, 7]], [[1, 2], [5, 9], [6, 11]]):
        a = np.array(values)
        medians, spread = panel_variability(a)
        assert np.allclose(medians, np.median(a, axis=1))
        assert np.allclose(spread, np.std(a, axis=0))
