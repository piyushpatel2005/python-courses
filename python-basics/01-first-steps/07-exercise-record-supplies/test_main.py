from solution import *
import solution as _solution

def test_packet_name():
    """Use text for the seed packet name"""
    assert type(packet_name) is str and packet_name == "Basil seeds", "Use the quoted text Basil seeds"

def test_packet_count():
    """Use a whole number for packet count"""
    assert type(packet_count) is int and packet_count == 6, "Use the integer 6"

def test_packet_price():
    """Use a decimal for packet price"""
    assert type(packet_price) is float and packet_price == 1.75, "Use the float 1.75"
