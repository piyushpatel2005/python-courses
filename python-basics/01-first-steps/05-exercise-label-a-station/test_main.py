from solution import *
import solution as _solution

def test_station():
    """Name the repair station"""
    assert station == "Bike repair", "Set station to the exact text Bike repair"

def test_table_number():
    """Use a numeric table number"""
    assert type(table_number) is int and table_number == 4, "Use the integer 4, not the string '4'"
