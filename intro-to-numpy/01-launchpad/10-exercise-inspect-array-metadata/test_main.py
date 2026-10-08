from solution import *
import numpy as np

def test_observation_metadata():
    """Describe axes, shape, total size and first axis"""
    assert describe_observation(np.array([[3, 4, 5], [6, 7, 8]])) == (2, (2, 3), 6, 2)
    assert describe_observation(np.array([[[1], [2]]])) == (3, (1, 2, 1), 2, 1)
