from solution import *
import solution as _solution

def test_supply_name():
    """Use text for the supply name"""
    assert type(supply_name) is str and supply_name == "Glow moss", "Use the quoted text Glow moss"

def test_supply_count():
    """Use a whole number for supply count"""
    assert type(supply_count) is int and supply_count == 6, "Use the integer 6"

def test_supply_weight():
    """Use a decimal for supply weight"""
    assert type(supply_weight) is float and supply_weight == 1.75, "Use the float 1.75"
