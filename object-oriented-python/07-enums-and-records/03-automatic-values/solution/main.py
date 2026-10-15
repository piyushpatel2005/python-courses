from enum import Enum, auto

class MatchPhase(Enum):
    LOBBY = auto()
    PLAY = auto()
    RESULTS = auto()


if __name__ == "__main__":
    try:
        print([member.value for member in MatchPhase])
    except (AttributeError, TypeError, ValueError, KeyError, NameError) as error:
        print("Not ready:", type(error).__name__, str(error))
