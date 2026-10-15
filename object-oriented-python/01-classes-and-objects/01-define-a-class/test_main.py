from solution import *


def test_tool_is_a_class():
    assert "Tool" in globals(), "Define the Tool class above the console probe."
    assert isinstance(Tool, type), "Tool must be a class, not an instance or a function."
    first, second = Tool(), Tool()
    assert isinstance(first, Tool) and isinstance(second, Tool)
    assert first is not second, "Calling Tool twice should create separate instances."
