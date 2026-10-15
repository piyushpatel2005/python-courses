class Pickup:
    pass

class QuestPickup(Pickup):
    pass


def direct_object_base(value):
    pass  # TODO: complete the requested behavior.


if __name__ == "__main__":
    try:
        print("Plain:", direct_object_base(Pickup()))
        print("Subclass:", direct_object_base(QuestPickup()))
    except Exception as error:
        print("Not ready:", type(error).__name__, str(error))
