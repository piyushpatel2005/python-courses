from dataclasses import dataclass
from enum import Enum

class CaseState(Enum):
    OPEN = "open"
    CLOSED = "closed"

@dataclass
class SupportCase:
    subject: str
    state: str = "open"


if __name__ == "__main__":
    try:
        case = SupportCase("Missing label")
        print(case.state, isinstance(case.state, CaseState))
    except (AttributeError, TypeError, ValueError, KeyError, NameError) as error:
        print("Not ready:", type(error).__name__, str(error))
