prefix = "GLOBAL"

class AssetLabel:
    prefix = "TOOL"

    def __init__(self, code):
        self.code = code

    def text(self):
        pass


# Supplied console probe: keep this below your implementation.
if __name__ == "__main__":
    try:
        first, second = AssetLabel("A1"), AssetLabel("B2")
        second.prefix = "REPAIR"
        print("Default:", first.text())
        print("Override:", second.text())
    except (NameError, AttributeError, TypeError, ValueError) as error:
        print("Not ready yet:", error)
