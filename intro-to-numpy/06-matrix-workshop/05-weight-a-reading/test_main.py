import numpy as np
from solution import *


def test_weight_a_reading():
    assert np.ndim(weighted) == 0 and weighted == np.dot(readings, weights)
