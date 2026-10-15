from enum import Enum

class GameTheme(Enum):
    LIGHT = "light"
    BRIGHT = "light"
    DARK = "dark"

def member_rows(enum_type):
    return None


if __name__ == "__main__":
    try:
        print(member_rows(GameTheme))
    except (AttributeError, TypeError, ValueError, KeyError, NameError) as error:
        print("Not ready:", type(error).__name__, str(error))
