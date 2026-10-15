prefix = "GLOBAL"

class ItemLabel:
    prefix = "ITEM"

    def __init__(self, code):
        self.code = code

    def text(self):
        pass


# Supplied console probe: keep this below your implementation.
if __name__ == "__main__":
    try:
        first, second = ItemLabel("A1"), ItemLabel("B2")
        second.prefix = "RARE"
        print("Default:", first.text())
        print("Override:", second.text())
    except (NameError, AttributeError, TypeError, ValueError) as error:
        print("Not ready yet:", error)
