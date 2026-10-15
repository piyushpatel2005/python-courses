class SaveSlot:
    def __init__(self, profile, number):
        self.profile = profile
        self.number = number

    def __eq__(self, other):
        pass  # TODO: complete the requested behavior.


if __name__ == "__main__":
    try:
        print("Equal save slots:", SaveSlot("C", 7) == SaveSlot("C", 7))
        print("Different profiles:", SaveSlot("C", 7) == SaveSlot("D", 7))
    except Exception as error:
        print("Not ready:", type(error).__name__, str(error))
