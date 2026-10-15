from enum import Enum

class ParcelCode(Enum):
    ACCEPTED = 0
    MISSING = 1


if __name__ == "__main__":
    try:
        print(ParcelCode.ACCEPTED.value, ParcelCode.MISSING.value)
    except (AttributeError, TypeError, ValueError, KeyError, NameError) as error:
        print("Not ready:", type(error).__name__, str(error))
