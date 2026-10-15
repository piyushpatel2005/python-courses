class Ticket:
    def __init__(self, title):
        self.title = title

    def label(self):
        return f"Ticket: {self.title}"

class TimedTicket(Ticket):
    def __init__(self, title, hour):
        super().__init__(title)
        self.hour = hour


if __name__ == "__main__":
    try:
        ticket = TimedTicket("Exhibit", 14)
        print(ticket.label(), ticket.hour)
    except Exception as error:
        print("Not ready:", type(error).__name__, str(error))
