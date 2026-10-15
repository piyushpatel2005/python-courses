from enum import Enum

class WorkState(Enum):
    WAITING = "waiting"
    COMPLETE = "complete"

def can_archive(state):
    return None


if __name__ == "__main__":
    try:
        print(can_archive(WorkState.COMPLETE), can_archive("complete"))
    except (AttributeError, TypeError, ValueError, KeyError, NameError) as error:
        print("Not ready:", type(error).__name__, str(error))
