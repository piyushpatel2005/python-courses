class Cable:
    def __init__(self, metres):
        self.metres = metres

    def __add__(self, other):
        pass  # TODO: complete the requested behavior.


if __name__ == "__main__":
    try:
        print("Combined metres:", (Cable(4) + Cable(6)).metres)
    except Exception as error:
        print("Not ready:", type(error).__name__, str(error))
