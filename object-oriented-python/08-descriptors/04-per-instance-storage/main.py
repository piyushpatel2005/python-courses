class StoredBadge:
    def __init__(self):
        self.key = "_badge"

    def __get__(self, instance, owner):
        if instance is None:
            return self
        return None

    def __set__(self, instance, value):
        pass

class PlayerProfile:
    badge = StoredBadge()


if __name__ == "__main__":
    try:
        left, right = PlayerProfile(), PlayerProfile()
        left.badge = "Pathfinder"
        right.badge = "Lantern keeper"
        print(left.badge, right.badge)
    except (AttributeError, TypeError, ValueError, KeyError, NameError) as error:
        print("Not ready:", type(error).__name__, str(error))
