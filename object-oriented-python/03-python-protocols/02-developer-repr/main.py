class LootBundle:
    def __init__(self, code, count):
        self.code = code
        self.count = count

    def __repr__(self):
        pass  # TODO: complete the requested behavior.


if __name__ == "__main__":
    try:
        print(repr(LootBundle("A'7", 3)))
    except Exception as error:
        print("Not ready:", type(error).__name__, str(error))
