from enum import Enum, unique

def make_abilities(first, second):
    @unique
    class AbilityChoice(Enum):
        FIRST = first
        SECOND = second
    return AbilityChoice


if __name__ == "__main__":
    try:
        print([item.value for item in make_abilities("dash", "heal")])
        try:
            make_abilities("dash", "dash")
        except ValueError:
            print("Duplicate rejected")
        else:
            print("Duplicate still accepted")
    except (AttributeError, TypeError, ValueError, KeyError, NameError) as error:
        print("Not ready:", type(error).__name__, str(error))
