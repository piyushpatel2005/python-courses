from dataclasses import dataclass
from enum import Enum

@dataclass(frozen=True)
class Dimensions:
    width: int
    height: int

class PaperSize(Enum):
    pass


if __name__ == "__main__":
    try:
        size = PaperSize.CARD.value
        print(size.width, size.height, size.width * size.height)
    except (AttributeError, TypeError, ValueError, KeyError, NameError) as error:
        print("Not ready:", type(error).__name__, str(error))
