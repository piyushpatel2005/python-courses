from dataclasses import dataclass
from enum import Enum

class QuestState(Enum):
    NEW = "new"
    DONE = "done"

@dataclass
class QuestEntry:
    title: str
    state: str = "new"


if __name__ == "__main__":
    try:
        entry = QuestEntry("Find the lantern")
        print(entry.state, isinstance(entry.state, QuestState))
    except (AttributeError, TypeError, ValueError, KeyError, NameError) as error:
        print("Not ready:", type(error).__name__, str(error))
