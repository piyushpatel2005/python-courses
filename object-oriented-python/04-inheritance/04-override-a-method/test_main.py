from solution import *


def test_01_override_a_method():
    assert issubclass(QuietAlarm, Alarm)
    assert "__init__" not in QuietAlarm.__dict__
    for location in ("door", "studio", "rear gate"):
        assert QuietAlarm(location).signal() == f"Light at {location}", "Override the subclass signal."
        assert Alarm(location).signal() == f"Sound at {location}"
    item = QuietAlarm("old")
    item.location = "new"
    assert item.signal() == "Light at new"
