from enum import Enum

class QuestState(Enum):
    NEW = "new"
    DONE = "done"

def is_quest_state(value):
    return None


if __name__ == "__main__":
    try:
        print(is_quest_state(QuestState.NEW), is_quest_state("new"))
    except (AttributeError, TypeError, ValueError, KeyError, NameError) as error:
        print("Not ready:", type(error).__name__, str(error))
