from enum import Enum

class QuestState(Enum):
    NEW = "new"
    DONE = "done"

def can_archive(state):
    return state is QuestState.DONE


if __name__ == "__main__":
    try:
        print(can_archive(QuestState.DONE), can_archive("done"))
    except (AttributeError, TypeError, ValueError, KeyError, NameError) as error:
        print("Not ready:", type(error).__name__, str(error))
