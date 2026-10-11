from solution import *
import solution as _solution

def test_charges():
    """1. Set the integer charge count"""
    assert type(charges) is int and charges == 5, "Set charges to the integer 5"


def test_weight():
    """2. Update the decimal weight"""
    assert type(weight) is float and weight == 3.5, "Set weight to the float 3.5"
