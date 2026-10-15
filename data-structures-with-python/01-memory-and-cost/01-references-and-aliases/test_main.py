from solution import *

def test_01_step():
    """Append the payload to the caller's list."""
    for initial in ([], [2], [2, 2]):
        items = list(initial)
        payload = []
        append_shared(items, payload)
        assert items[:-1] == initial and items[-1] is payload

def test_02_complete_operation():
    """Append once while preserving the caller's list identity."""
    for initial in ([], [2], [2, 2], ["map", "pen"]):
        items = list(initial)
        alias = items
        value = []
        result = append_shared(items, value)
        assert result is items and alias is items
        assert items[:-1] == initial and items[-1] is value
        append_shared(items, value)
        assert len(items) == len(initial) + 2 and items[-2] is value
    separate = []
    append_shared(separate, 9)
    assert separate == [9]
