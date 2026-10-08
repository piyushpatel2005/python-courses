from solution import *
import numpy as np

def test_extra_tick():
    """The countdown includes eight"""
    assert ticks.tolist() == [2, 4, 6, 8] and points.tolist() == [0.0, 0.5, 1.0]
