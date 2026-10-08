from solution import *
import numpy as np

def test_wave():
    """Find sine for each angle in radians"""
    assert np.allclose(wave, [0, 1])
