import numpy as np
from solution import *


def test_exercise_sensor_extremes():
    for values in ([9, 3, 14, 6], [21, 4, 4, 12, 30]):
        a = np.array(values)
        assert tuple(extremes(a)) == (np.sum(a), np.min(a), np.max(a), np.argmin(a), np.argmax(a))
