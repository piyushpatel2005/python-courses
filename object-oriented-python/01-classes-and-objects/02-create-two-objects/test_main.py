from solution import *


def test_two_separate_tools():
    assert isinstance(drill, Tool), "Create drill with a Tool call."
    assert isinstance(saw, Tool), "Create saw with a separate Tool call."
    assert drill is not saw, "Two names for one object are not two tools."
    drill.check_label = "first"
    assert not hasattr(saw, "check_label"), "The tools must have independent identities."
