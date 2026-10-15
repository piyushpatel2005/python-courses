from enum import Enum

class QuestCode(Enum):
    ACCEPTED = 202
    MISSING = 404


if __name__ == "__main__":
    try:
        print(QuestCode.ACCEPTED.value, QuestCode.MISSING.value)
    except (AttributeError, TypeError, ValueError, KeyError, NameError) as error:
        print("Not ready:", type(error).__name__, str(error))
