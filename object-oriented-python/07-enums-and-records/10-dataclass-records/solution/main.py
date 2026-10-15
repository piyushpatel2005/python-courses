from dataclasses import dataclass

@dataclass
class Reading:
    title: str
    pages: int = 0


if __name__ == "__main__":
    try:
        first = Reading("River notes", 18)
        print(first)
        print(first == Reading("River notes", 18))
    except (AttributeError, TypeError, ValueError, KeyError, NameError) as error:
        print("Not ready:", type(error).__name__, str(error))
