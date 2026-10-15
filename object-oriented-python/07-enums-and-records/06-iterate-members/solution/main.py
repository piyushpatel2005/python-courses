from enum import Enum

class Theme(Enum):
    LIGHT = "light"
    BRIGHT = "light"
    DARK = "dark"

def member_rows(enum_type):
    return [(member.name, member.value) for member in enum_type]


if __name__ == "__main__":
    try:
        print(member_rows(Theme))
    except (AttributeError, TypeError, ValueError, KeyError, NameError) as error:
        print("Not ready:", type(error).__name__, str(error))
