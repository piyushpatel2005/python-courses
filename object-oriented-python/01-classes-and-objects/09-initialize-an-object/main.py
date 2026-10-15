class Tool:
    def __init__(self, name, uses):
        pass

    def summary(self):
        return f"{self.name}: {self.uses} uses"


# Supplied console probe: keep this below your implementation.
if __name__ == "__main__":
    try:
        print(Tool("drill", 4).summary())
        print(Tool("saw", 1).summary())
    except (NameError, AttributeError, TypeError, ValueError) as error:
        print("Not ready yet:", error)
