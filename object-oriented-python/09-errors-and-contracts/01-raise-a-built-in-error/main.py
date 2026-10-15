class Reservation:
    def __init__(self):
        self.seats = 1

    def set_seats(self, count):
        pass


if __name__ == "__main__":
    try:
        r = Reservation()
        r.set_seats(4)
        print("Seats:", r.seats)
    except Exception as error:
        print("Probe:", type(error).__name__, str(error))
