from solution import *


def test_description_is_attached_without_execution():
    calls = []
    def first():
        calls.append("first")
        return 42
    def second():
        calls.append("second")
        return "ready"
    set_description(first, "Count inventory")
    set_description(second, "Open map")
    assert getattr(first, "description", None) == "Count inventory", "Attach metadata to the function object."
    assert second.description == "Open map" and calls == []
    set_description(first, "Recount")
    assert first.description == "Recount" and second.description == "Open map"
    assert first() == 42 and second() == "ready" and calls == ["first", "second"]
