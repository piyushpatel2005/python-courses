import numpy as np
from solution import *


def test_describe_a_series():
    assert np.isclose(spread, np.std(temperatures)) and not np.isclose(spread, np.mean(temperatures))
