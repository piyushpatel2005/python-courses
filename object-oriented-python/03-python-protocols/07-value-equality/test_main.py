from solution import *


def test_01_value_equality():
    for row, number in (("A", 1), ("Z", 20), ("AA", 0)):
        first, second = Seat(row, number), Seat(row, number)
        assert first is not second and first == second, "Compare both stored fields."
        assert first != Seat(row + "X", number)
        assert first != Seat(row, number + 1)
        second.number += 1
        assert first != second
    assert Seat("A", 1).__eq__(("A", 1)) is NotImplemented
    assert (Seat("A", 1) == "A1") is False
    class Other:
        def __eq__(self, other):
            return "other comparison"
    assert (Seat("A", 1) == Other()) == "other comparison"
    try:
        hash(Seat("A", 1))
    except TypeError:
        pass
    else:
        assert False, "Keep mutable seats unhashable."
