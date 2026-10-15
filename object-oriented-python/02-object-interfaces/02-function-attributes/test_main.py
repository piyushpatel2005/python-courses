from solution import *


def test_description_is_attached_without_execution():
    calls = []
    def first():
        calls.append("first")
        return 42
    def second():
        calls.append("second")
        return "ready"
    set_description(first, "Count stock")
    set_description(second, "Open desk")
    assert getattr(first, "description", None) == "Count stock", "Attach metadata to the function object."
    assert second.description == "Open desk" and calls == []
    set_description(first, "Recount")
    assert first.description == "Recount" and second.description == "Open desk"
    assert first() == 42 and second() == "ready" and calls == ["first", "second"]
