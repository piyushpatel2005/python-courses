from solution import *
import numpy as np

def test_taller_blank():
    """Blank panel is three by four"""
    assert blank.shape == (3, 4) and np.all(blank == 0)
