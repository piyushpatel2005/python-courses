from solution import *


def test_each_tool_keeps_its_name():
    tools = [make_tool(value) for value in ("drill", "saw", "", "clamp")]
    assert all(isinstance(tool, Tool) for tool in tools)
    assert [getattr(tool, "name", None) for tool in tools] == ["drill", "saw", "", "clamp"], "Store the name parameter on each tool."
    tools[0].name = "changed"
    assert tools[1].name == "saw", "Names belong to separate instances."
