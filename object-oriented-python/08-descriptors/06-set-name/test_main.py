from solution import *


def test_set_name():
    assert Contact.city.key == "_city" and Contact.region.key == "_region"
    a, b = Contact(), Contact()
    a.city, a.region, b.city = "Oslo", "East", "Lima"
    assert (a.city, a.region, b.city, b.region) == ("Oslo", "East", "Lima", None)
    class Other:
        zone = NamedField()
        code = NamedField()
    other = Other()
    other.zone, other.code = 3, "Z"
    assert (other.zone, other.code) == (3, "Z")
    assert Other.zone.key == "_zone"
