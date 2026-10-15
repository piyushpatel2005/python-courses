class Inventory:
    def __init__(self, items):
        self.items = list(items)

    def __len__(self):
        pass  # TODO: complete the requested behavior.


if __name__ == "__main__":
    try:
        inventory = Inventory(["Map", "Lantern"])
        print("Items:", len(inventory))
        inventory.items.append("Rope")
        print("After adding:", len(inventory))
    except Exception as error:
        print("Not ready:", type(error).__name__, str(error))
