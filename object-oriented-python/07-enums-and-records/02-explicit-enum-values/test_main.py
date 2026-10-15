from solution import *


def test_explicit_enum_values():
    assert ParcelCode.ACCEPTED.value == 202
    assert ParcelCode.MISSING.value == 404
    assert ParcelCode(202) is ParcelCode.ACCEPTED
    assert ParcelCode["MISSING"] is ParcelCode.MISSING
    try:
        ParcelCode(999)
    except ValueError:
        pass
    else:
        assert False, "An unknown code must not become a new member"
