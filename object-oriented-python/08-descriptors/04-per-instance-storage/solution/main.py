class StoredCode:
    def __init__(self):
        self.key = "_code"

    def __get__(self, instance, owner):
        if instance is None:
            return self
        return instance.__dict__.get(self.key)

    def __set__(self, instance, value):
        instance.__dict__[self.key] = value

class Locker:
    code = StoredCode()


if __name__ == "__main__":
    try:
        left, right = Locker(), Locker()
        left.code = "A7"
        right.code = "B2"
        print(left.code, right.code)
    except (AttributeError, TypeError, ValueError, KeyError, NameError) as error:
        print("Not ready:", type(error).__name__, str(error))
