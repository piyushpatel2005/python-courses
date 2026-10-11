from solution import describe_observation
import numpy as np


def test_observation_metadata():
    """Return the four measurements in the requested order"""
    cases = [
        (np.array([[3, 4, 5], [6, 7, 8]]), (2, (2, 3), 6, 2)),
        (np.array([[[1], [2]]]), (3, (1, 2, 1), 2, 1)),
        (np.array([7, 9, 11]), (1, (3,), 3, 3)),
    ]
    for observation, expected in cases:
        result = describe_observation(observation)
        assert isinstance(result, tuple), "Return a tuple rather than None or a printed message."
        assert result == expected, "Return ndim, shape, size, and len(observation), in that order, for the supplied array."
