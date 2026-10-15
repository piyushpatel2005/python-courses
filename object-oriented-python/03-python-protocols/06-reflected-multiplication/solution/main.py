class TokenPack:
    def __init__(self, count):
        self.count = count

    def __mul__(self, factor):
        if type(factor) is not int:
            return NotImplemented
        return TokenPack(self.count * factor)

    def __rmul__(self, factor):
        return self.__mul__(factor)


if __name__ == "__main__":
    try:
        pack = TokenPack(5)
        print("Both orders:", (pack * 4).count, (4 * pack).count)
    except Exception as error:
        print("Not ready:", type(error).__name__, str(error))
