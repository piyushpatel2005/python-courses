from solution import *
import numpy as np

def test_blank_panel():
    """Blank panel has the requested shape and zeros"""
    for shape in [(2, 3), (1, 4)]:
        panel = blank_panel(*shape)
        assert isinstance(panel, np.ndarray) and panel.shape == shape and np.all(panel == 0)

def test_active_panel():
    """Active panel has the requested shape and ones"""
    for shape in [(3, 2), (1, 5)]:
        panel = active_panel(*shape)
        assert isinstance(panel, np.ndarray) and panel.shape == shape and np.all(panel == 1)
