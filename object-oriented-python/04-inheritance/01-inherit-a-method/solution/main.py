class Locker:
    def __init__(self, code):
        self.code = code

    def label(self):
        return f"Locker {self.code}"

class ColdLocker(Locker):
    pass


if __name__ == "__main__":
    try:
        item = ColdLocker("B7")
        print(item.label())
        print("Is a locker:", isinstance(item, Locker))
    except Exception as error:
        print("Not ready:", type(error).__name__, str(error))
