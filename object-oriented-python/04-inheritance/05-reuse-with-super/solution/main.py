class Shipment:
    def __init__(self, tracking):
        self.tracking = tracking

    def label(self):
        return f"Shipment {self.tracking}"

class InsuredShipment(Shipment):
    def __init__(self, tracking, amount):
        super().__init__(tracking)
        self.amount = amount

    def label(self):
        return super().label() + f" | insured {self.amount}"


if __name__ == "__main__":
    try:
        print(InsuredShipment("Q8", 200).label())
    except Exception as error:
        print("Not ready:", type(error).__name__, str(error))
