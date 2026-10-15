from solution import *


def test_01_friendly_str():
    for destination, km in (("Ridge", 9), ("Gate", 0), ("Pond", 2.5)):
        marker = TrailMarker(destination, km)
        assert str(marker) == f"{destination}: {km} km", "Return a label from this marker's attributes."
        marker.km = 12
        assert str(marker) == f"{destination}: 12 km"
