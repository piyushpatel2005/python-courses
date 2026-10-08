from solution import *
import numpy as np

def test_third_row():
    """The board has three rows and two columns"""
    assert levels.shape == (3, 2) and levels[-1].tolist() == [7, 8]
