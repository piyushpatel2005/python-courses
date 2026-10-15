from solution import *


def test_compare_members():
    from enum import Enum
    class Other(Enum):
        COMPLETE = "complete"
    for item, expected in [(WorkState.COMPLETE, True), (WorkState.WAITING, False), ("complete", False), (Other.COMPLETE, False), (None, False), (1, False)]:
        assert can_archive(item) is expected, "Recognize only WorkState.COMPLETE"
