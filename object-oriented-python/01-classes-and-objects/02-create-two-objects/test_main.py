from solution import *


def test_two_separate_items():
    assert isinstance(lantern, GameItem), "Create lantern with a GameItem call."
    assert isinstance(shield, GameItem), "Create shield with a separate GameItem call."
    assert lantern is not shield, "Two names for one object are not two items."
    lantern.check_label = "first"
    assert not hasattr(shield, "check_label"), "The items must have independent identities."
