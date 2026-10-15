class GameEntity:
    def __init__(self, code):
        self.code = code

    def label(self):
        return f"GameEntity {self.code}"

# TODO: define the requested subclass here.
pass


if __name__ == "__main__":
    try:
        item = SupplyChest("B7")
        print(item.label())
        print("Is a game entity:", isinstance(item, GameEntity))
    except Exception as error:
        print("Not ready:", type(error).__name__, str(error))
