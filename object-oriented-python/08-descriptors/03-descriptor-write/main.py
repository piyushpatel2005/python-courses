class ManaAmount:
    def __get__(self, instance, owner):
        if instance is None:
            return self
        return instance.__dict__.get("_mana", 0)

    def __set__(self, instance, value):
        pass

class ManaPool:
    mana = ManaAmount()


if __name__ == "__main__":
    try:
        item = ManaPool()
        item.mana = 7
        print(item.mana)
        try:
            item.mana = -1
        except ValueError:
            print("Rejected:", item.mana)
        else:
            print("Negative value accepted")
    except (AttributeError, TypeError, ValueError, KeyError, NameError) as error:
        print("Not ready:", type(error).__name__, str(error))
