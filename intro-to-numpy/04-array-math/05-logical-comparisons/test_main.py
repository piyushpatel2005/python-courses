from solution import *
import numpy as np

def test_band():
    """Keep values between five and ten"""
    assert np.array_equal(usable, [False, True, True, False])
