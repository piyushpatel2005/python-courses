class Seat:
    def __init__(self, row, number):
        self.row = row
        self.number = number

    def __eq__(self, other):
        pass  # TODO: complete the requested behavior.


if __name__ == "__main__":
    try:
        print("Equal seats:", Seat("C", 7) == Seat("C", 7))
        print("Different rows:", Seat("C", 7) == Seat("D", 7))
    except Exception as error:
        print("Not ready:", type(error).__name__, str(error))
