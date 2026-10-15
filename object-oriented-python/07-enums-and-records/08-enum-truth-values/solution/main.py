from enum import Enum

class ScreenShake(Enum):
    OFF = 0
    LOW = 2
    HIGH = 5

    def __bool__(self):
        return bool(self.value)


if __name__ == "__main__":
    try:
        print(bool(ScreenShake.OFF), bool(ScreenShake.LOW), bool(ScreenShake.HIGH))
    except (AttributeError, TypeError, ValueError, KeyError, NameError) as error:
        print("Not ready:", type(error).__name__, str(error))
