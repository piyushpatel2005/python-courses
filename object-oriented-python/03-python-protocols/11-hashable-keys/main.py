class SaveSlotKey:
    __slots__ = ("_parts",)

    def __init__(self, profile, number):
        if hasattr(self, "_parts"):
            raise AttributeError("SaveSlotKey is already initialized")
        if type(profile) is not str or type(number) is not int:
            raise TypeError("profile must be str and number must be int")
        object.__setattr__(self, "_parts", (profile, number))

    def __setattr__(self, name, value):
        raise AttributeError("SaveSlotKey is immutable")

    def __delattr__(self, name):
        raise AttributeError("SaveSlotKey is immutable")

    @property
    def profile(self):
        return self._parts[0]

    @property
    def number(self):
        return self._parts[1]

    def __eq__(self, other):
        if type(other) is not type(self):
            return NotImplemented
        return self._parts == other._parts

    def __hash__(self):
        pass  # TODO: complete the requested behavior.


if __name__ == "__main__":
    try:
        saves = {SaveSlotKey("west", 4): "checkpoint"}
        print("Found:", saves[SaveSlotKey("west", 4)])
    except Exception as error:
        print("Not ready:", type(error).__name__, str(error))
