from dataclasses import dataclass

@dataclass
class PlayerSave:
    player_name: str
    experience: int = 0


if __name__ == "__main__":
    try:
        first = PlayerSave("Mira", 18)
        print(first)
        print(first == PlayerSave("Mira", 18))
    except (AttributeError, TypeError, ValueError, KeyError, NameError) as error:
        print("Not ready:", type(error).__name__, str(error))
