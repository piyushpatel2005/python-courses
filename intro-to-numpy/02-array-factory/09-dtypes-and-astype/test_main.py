from solution import *
import numpy as np

def test_off_channel():
    """Middle channel converts to False"""
    assert flags.tolist() == [False, False, True] and flags.dtype.kind == 'b'
