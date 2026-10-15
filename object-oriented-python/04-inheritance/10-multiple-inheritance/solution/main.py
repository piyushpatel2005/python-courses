class PrintableCode:
    def print_label(self):
        return f"Item {self.code}"

class TrackableCode:
    def tracking_path(self):
        return f"/track/{self.code}"

class InventoryCard(PrintableCode, TrackableCode):
    def __init__(self, code):
        self.code = code


if __name__ == "__main__":
    try:
        card = InventoryCard("K9")
        print(card.print_label())
        print(card.tracking_path())
    except Exception as error:
        print("Not ready:", type(error).__name__, str(error))
