from enum import Enum

class QuestState(Enum):
    pass


if __name__ == "__main__":
    try:
        print(QuestState.NEW.name, QuestState.DONE.value)
    except (AttributeError, TypeError, ValueError, KeyError, NameError) as error:
        print("Not ready:", type(error).__name__, str(error))
