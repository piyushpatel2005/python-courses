class Delivery:
    def __init__(self, code):
        self.code = code

    def dispatch(self):
        return f"Road {self.code}"

class BikeDelivery(Delivery):
    def dispatch(self):
        return f"Bike {self.code}"


def dispatch_messages(deliveries):
    return [delivery.dispatch() for delivery in deliveries]


if __name__ == "__main__":
    try:
        print(dispatch_messages([Delivery("A"), BikeDelivery("B")]))
    except Exception as error:
        print("Not ready:", type(error).__name__, str(error))
