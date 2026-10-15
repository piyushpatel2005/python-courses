from solution import *


def test_notes_are_independent_lists():
    first, second = Tool("drill"), Tool("saw")
    assert getattr(first, "notes", None) == [], "Create an empty notes list in __init__."
    assert isinstance(first.notes, list) and isinstance(second.notes, list)
    assert first.notes is not second.notes, "Each initializer call needs a fresh list."
    first.add_note("cleaned")
    first.add_note("oiled")
    assert first.notes == ["cleaned", "oiled"] and second.notes == []
    second.add_note("sharpened")
    assert first.notes == ["cleaned", "oiled"] and second.notes == ["sharpened"]
    assert Tool("plane").notes == []
