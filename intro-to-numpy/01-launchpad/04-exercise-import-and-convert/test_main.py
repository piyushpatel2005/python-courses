from solution import *
import numpy as np

def test_make_feed():
    """Different feeds become arrays with their own values"""
    assert isinstance(make_feed([11, 14, 17]), np.ndarray)
    assert make_feed([11, 14, 17]).tolist() == [11, 14, 17]
    assert make_feed([2, 8]).tolist() == [2, 8]
