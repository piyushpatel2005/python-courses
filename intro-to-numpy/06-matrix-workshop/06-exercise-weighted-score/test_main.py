import numpy as np
from solution import *


def test_exercise_weighted_score():
    for scores, weights in [([5, 2, 4], [2, 3, 1]), ([3, 8], [4, 2])]:
        assert np.ndim(weighted_score(np.array(scores), np.array(weights))) == 0
        assert weighted_score(np.array(scores), np.array(weights)) == np.dot(scores, weights)
