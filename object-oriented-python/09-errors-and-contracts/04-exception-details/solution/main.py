class InventoryShortage(Exception):
    def __init__(self, requested, available):
        self.requested = requested
        self.available = available
        super().__init__(f"inventory requested {requested}; available {available}")


if __name__ == "__main__":
    try:
        print(InventoryShortage(6, 2))
    except Exception as error:
        print("Probe:", type(error).__name__, str(error))
