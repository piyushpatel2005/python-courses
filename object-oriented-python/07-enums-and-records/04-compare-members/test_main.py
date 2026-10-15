from solution import *


def test_compare_members():
    from enum import Enum
    class Other(Enum):
        DONE = "done"
    for item, expected in [(QuestState.DONE, True), (QuestState.NEW, False), ("done", False), (Other.DONE, False), (None, False), (1, False)]:
        assert can_archive(item) is expected, "Recognize only QuestState.DONE"
