from solution import *


def test_01_hashable_keys():
    for profile, number in (("east", 2), ("west", 0), ("", -7)):
        key, equal_key = SaveSlotKey(profile, number), SaveSlotKey(profile, number)
        assert hash(key) == hash((profile, number)), "Hash the tuple of equality fields."
        assert hash(key) == hash(equal_key)
        mapping = {key: "stored"}
        assert mapping[equal_key] == "stored"
        assert len({key, equal_key}) == 1
        for field, value in (("profile", "changed"), ("number", 99), ("_parts", ("other", 7))):
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
    assert SaveSlotKey("east", 1) != SaveSlotKey("west", 1)
    assert SaveSlotKey("east", 1).__eq__(("east", 1)) is NotImplemented
