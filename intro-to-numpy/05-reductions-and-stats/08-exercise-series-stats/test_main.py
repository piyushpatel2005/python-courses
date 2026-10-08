import numpy as np
from solution import *


def test_exercise_series_stats():
    for values in ([40., 44., 48.], [2., 3., 3., 12.]):
        a = np.array(values)
        assert np.allclose(describe(a), (np.mean(a), np.median(a), np.var(a), np.std(a)))
