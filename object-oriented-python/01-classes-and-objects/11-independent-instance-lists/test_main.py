from solution import *


def test_notes_are_independent_lists():
    first, second = GameItem("lantern"), GameItem("shield")
    assert getattr(first, "notes", None) == [], "Create an empty notes list in __init__."
    assert isinstance(first.notes, list) and isinstance(second.notes, list)
    assert first.notes is not second.notes, "Each initializer call needs a fresh list."
    first.add_note("glow adjusted")
    first.add_note("range tested")
    assert first.notes == ["glow adjusted", "range tested"] and second.notes == []
    second.add_note("block tested")
    assert first.notes == ["glow adjusted", "range tested"] and second.notes == ["block tested"]
    assert GameItem("horn").notes == []
