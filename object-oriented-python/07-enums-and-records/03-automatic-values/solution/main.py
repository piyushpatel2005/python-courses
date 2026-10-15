from enum import Enum, auto

class PackPhase(Enum):
    PICK = auto()
    WRAP = auto()
    SEND = auto()


if __name__ == "__main__":
    try:
        print([member.value for member in PackPhase])
    except (AttributeError, TypeError, ValueError, KeyError, NameError) as error:
        print("Not ready:", type(error).__name__, str(error))
