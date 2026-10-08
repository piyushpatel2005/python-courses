import numpy as np
from solution import *


def test_running_totals():
    assert np.array_equal(running, np.cumsum(sightings))
