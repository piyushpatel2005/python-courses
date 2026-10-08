from solution import *
import numpy as np

def test_last_score():
    """The last score is 12"""
    assert isinstance(scores, np.ndarray) and scores.tolist() == [4, 6, 12]
