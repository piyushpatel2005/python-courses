import numpy as np
from solution import *


def test_sort_a_grid():
    assert np.array_equal(by_microphone, np.sort(samples, axis=1))
