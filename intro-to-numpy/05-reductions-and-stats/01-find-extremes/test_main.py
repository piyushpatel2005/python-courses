import numpy as np
from solution import *


def test_find_extremes():
    assert loudest == np.max(readings)
