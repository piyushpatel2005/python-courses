from enum import Enum

class Signal(Enum):
    OFF = 0
    LOW = 2
    HIGH = 5

    def __bool__(self):
        return True


if __name__ == "__main__":
    try:
        print(bool(Signal.OFF), bool(Signal.LOW), bool(Signal.HIGH))
    except (AttributeError, TypeError, ValueError, KeyError, NameError) as error:
        print("Not ready:", type(error).__name__, str(error))
