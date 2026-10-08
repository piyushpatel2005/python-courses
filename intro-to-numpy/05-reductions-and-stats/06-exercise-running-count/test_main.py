import numpy as np
from solution import *


def test_exercise_running_count():
    for values in ([2, 5, 1], [8, 0, 3, 6]):
        assert np.array_equal(running_count(np.array(values)), np.cumsum(values))
