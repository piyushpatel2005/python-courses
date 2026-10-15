from solution import *


def test_named_statuses():
    from enum import Enum
    assert issubclass(QuestState, Enum)
    assert list(QuestState.__members__) == ["NEW", "DONE"]
    assert QuestState.NEW.value == "new"
    assert QuestState.DONE.value == "done"
    assert QuestState.NEW is not QuestState.DONE
