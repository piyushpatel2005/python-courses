from enum import Enum, unique

def make_choices(first, second):
    class Choice(Enum):
        FIRST = first
        SECOND = second
    return Choice


if __name__ == "__main__":
    try:
        print([item.value for item in make_choices("tea", "juice")])
        try:
            make_choices("tea", "tea")
        except ValueError:
            print("Duplicate rejected")
        else:
            print("Duplicate still accepted")
    except (AttributeError, TypeError, ValueError, KeyError, NameError) as error:
        print("Not ready:", type(error).__name__, str(error))
