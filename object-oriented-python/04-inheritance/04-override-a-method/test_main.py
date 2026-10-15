from solution import *


def test_01_override_a_method():
    assert issubclass(LightBeacon, Beacon)
    assert "__init__" not in LightBeacon.__dict__
    for location in ("door", "studio", "rear gate"):
        assert LightBeacon(location).signal() == f"Light at {location}", "Override the subclass signal."
        assert Beacon(location).signal() == f"Sound at {location}"
    item = LightBeacon("old")
    item.location = "new"
    assert item.signal() == "Light at new"
