class BinKey:
    __slots__ = ("_parts",)

    def __init__(self, zone, number):
        if hasattr(self, "_parts"):
            raise AttributeError("BinKey is already initialized")
        if type(zone) is not str or type(number) is not int:
            raise TypeError("zone must be str and number must be int")
        object.__setattr__(self, "_parts", (zone, number))

    def __setattr__(self, name, value):
        raise AttributeError("BinKey is immutable")

    def __delattr__(self, name):
        raise AttributeError("BinKey is immutable")

    @property
    def zone(self):
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
        stock = {BinKey("west", 4): "cables"}
        print("Found:", stock[BinKey("west", 4)])
    except Exception as error:
        print("Not ready:", type(error).__name__, str(error))
