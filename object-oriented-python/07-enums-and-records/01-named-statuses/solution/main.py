from enum import Enum

class TicketState(Enum):
    NEW = "new"
    DONE = "done"


if __name__ == "__main__":
    try:
        print(TicketState.NEW.name, TicketState.DONE.value)
    except (AttributeError, TypeError, ValueError, KeyError, NameError) as error:
        print("Not ready:", type(error).__name__, str(error))
