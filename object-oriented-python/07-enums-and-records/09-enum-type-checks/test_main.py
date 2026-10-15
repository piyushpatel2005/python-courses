from solution import *


def test_enum_type_checks():
    from enum import Enum
    class Other(Enum):
        NEW = "new"
    for value in QuestState:
        assert is_quest_state(value) is True
    for value in ["new", 0, None, QuestState, Other.NEW, object()]:
        assert is_quest_state(value) is False
