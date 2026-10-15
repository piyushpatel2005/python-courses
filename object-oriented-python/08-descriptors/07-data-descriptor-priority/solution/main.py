class Serial:
    def __get__(self, instance, owner):
        if instance is None:
            return self
        return instance.number

    def __set__(self, instance, value):
        raise AttributeError("Serial is read-only")

class PlayerBadge:
    serial = Serial()

    def __init__(self, number):
        self.number = number


if __name__ == "__main__":
    try:
        badge = PlayerBadge("R17")
        badge.__dict__["serial"] = "shadow"
        print(badge.serial)
    except (AttributeError, TypeError, ValueError, KeyError, NameError) as error:
        print("Not ready:", type(error).__name__, str(error))
