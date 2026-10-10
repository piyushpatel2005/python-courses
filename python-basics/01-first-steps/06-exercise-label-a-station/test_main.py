from solution import *
import solution as _solution

def test_beacon():
    """Name the beacon marker"""
    assert beacon == "North beacon", "Set beacon to the exact text North beacon"

def test_beacon_number():
    """Use a numeric beacon number"""
    assert type(beacon_number) is int and beacon_number == 4, "Use the integer 4, not the string '4'"
