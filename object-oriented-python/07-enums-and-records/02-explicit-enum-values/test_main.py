from solution import *


def test_explicit_enum_values():
    assert QuestCode.ACCEPTED.value == 202
    assert QuestCode.MISSING.value == 404
    assert QuestCode(202) is QuestCode.ACCEPTED
    assert QuestCode["MISSING"] is QuestCode.MISSING
    try:
        QuestCode(999)
    except ValueError:
        pass
    else:
        assert False, "An unknown code must not become a new member"
