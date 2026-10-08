from solution import *
import numpy as np

def test_selected():
    """Gather the first and third samples"""
    assert np.array_equal(selected, np.array([12, 15]))
