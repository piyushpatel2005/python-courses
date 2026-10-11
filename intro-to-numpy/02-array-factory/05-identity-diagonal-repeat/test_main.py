from solution import *
import numpy as np

def test_four_channel_cue():
    """Identity cue has four diagonal ones"""
    assert cue.shape == (4, 4) and np.array_equal(cue, np.eye(4))
