from solution import *


def test_01_value_equality():
    for profile, number in (("A", 1), ("Z", 20), ("AA", 0)):
        first, second = SaveSlot(profile, number), SaveSlot(profile, number)
        assert first is not second and first == second, "Compare both stored fields."
        assert first != SaveSlot(profile + "X", number)
        assert first != SaveSlot(profile, number + 1)
        second.number += 1
        assert first != second
    assert SaveSlot("A", 1).__eq__(("A", 1)) is NotImplemented
    assert (SaveSlot("A", 1) == "A1") is False
    class Other:
        def __eq__(self, other):
            return "other comparison"
    assert (SaveSlot("A", 1) == Other()) == "other comparison"
    try:
        hash(SaveSlot("A", 1))
    except TypeError:
        pass
    else:
        assert False, "Keep mutable save slots unhashable."
