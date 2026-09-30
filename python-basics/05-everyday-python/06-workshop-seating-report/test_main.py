from solution import *


def test_seat_total():
    """Count seats from a list"""
    assert seat_total([2, 1, 3]) == 6, "Add all seat counts."
    assert seat_total([]) == 0, "The empty list totals zero."


def test_remaining_seats():
    """Available seats never go below zero"""
    assert remaining_seats(8, 3) == 5, "Subtract reserved from capacity."
    assert remaining_seats(8, 8) == 0, "A full workshop has zero available seats."
    assert remaining_seats(8, 10) == 0, "An overbooked workshop has zero available seats."


def test_workshop_report():
    """The report combines both helpers into one line"""
    assert workshop_report("Ceramics", 8, [2, 1]) == "Ceramics: 3 reserved, 5 available", "Use both helpers to build the report."
    assert workshop_report("Dance", 2, [1, 2]) == "Dance: 3 reserved, 0 available", "Use the actual name and never report negative availability."
