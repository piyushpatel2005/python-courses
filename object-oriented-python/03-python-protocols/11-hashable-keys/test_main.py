from solution import *


def test_01_hashable_keys():
    for zone, number in (("east", 2), ("west", 0), ("", -7)):
        key, equal_key = BinKey(zone, number), BinKey(zone, number)
        assert hash(key) == hash((zone, number)), "Hash the tuple of equality fields."
        assert hash(key) == hash(equal_key)
        mapping = {key: "stored"}
        assert mapping[equal_key] == "stored"
        assert len({key, equal_key}) == 1
        for field, value in (("zone", "changed"), ("number", 99), ("_parts", ("other", 7))):
            try:
                setattr(key, field, value)
            except AttributeError:
                pass
            else:
                assert False, "Hash fields must stay immutable."
        try:
            del key._parts
        except AttributeError:
            pass
        else:
            assert False, "Do not allow deletion of hash fields."
        try:
            key.__init__("changed", 99)
        except AttributeError:
            pass
        else:
            assert False, "Reinitialization must not change a stored key."
        assert mapping[equal_key] == "stored"
    assert BinKey("east", 1) != BinKey("west", 1)
    assert BinKey("east", 1).__eq__(("east", 1)) is NotImplemented
