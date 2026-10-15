from solution import *


def test_summary_returns_current_data():
    import contextlib
    import io
    output = io.StringIO()
    with contextlib.redirect_stdout(output):
        for name, count in (("drill", 0), ("saw", 19), ("hand plane", 1)):
            tool = make_tool(name, count)
            assert tool.summary() == f"{name}: {count} uses", "Return the formatted string instead of printing it."
            assert tool.name == name and tool.uses == count
            tool.uses += 2
            assert tool.summary() == f"{name}: {count + 2} uses"
    assert output.getvalue() == "", "summary should return text without printing."
