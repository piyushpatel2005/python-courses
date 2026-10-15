class CachedBadge:
    key = "_badge"

    def __get__(self, instance, owner):
        if instance is None:
            return self
        return instance.__dict__.get(self.key)

    def __set__(self, instance, value):
        instance.__dict__[self.key] = value

    def __delete__(self, instance):
        pass

class PlayerProfile:
    badge = CachedBadge()


if __name__ == "__main__":
    try:
        first, second = PlayerProfile(), PlayerProfile()
        first.badge, second.badge = "Scout", "Guide"
        del first.badge
        print(first.badge, second.badge)
    except (AttributeError, TypeError, ValueError, KeyError, NameError) as error:
        print("Not ready:", type(error).__name__, str(error))
