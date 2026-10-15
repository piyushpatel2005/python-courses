from solution import *


def test_display_name_is_a_live_property():
    assert isinstance(vars(Player).get("display_name"), property), "Place @property immediately above the getter."
    first, second = Player("Ari", "Shah"), Player("Jo", "Lee")
    assert first.display_name == "Ari Shah" and second.display_name == "Jo Lee"
    first.last = "Patel"
    second.first = "Kim"
    assert first.display_name == "Ari Patel" and second.display_name == "Kim Lee"
