from solution import *


def test_summary_returns_current_data():
    import contextlib
    import io
    output = io.StringIO()
    with contextlib.redirect_stdout(output):
        for name, count in (("lantern", 0), ("shield", 19), ("signal horn", 1)):
            item = make_item(name, count)
            assert item.summary() == f"{name}: {count} uses", "Return the formatted string instead of printing it."
            assert item.name == name and item.uses == count
            item.uses += 2
            assert item.summary() == f"{name}: {count + 2} uses"
    assert output.getvalue() == "", "summary should return text without printing."
