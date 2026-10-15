class Tool:
    def __init__(self, name, uses):
        self.name = name
        self.uses = uses


# Supplied console probe: keep this below your implementation.
if __name__ == "__main__":
    try:
        print("New tool uses:", Tool("drill").uses)
        print("Imported tool uses:", Tool("saw", uses=6).uses)
    except (NameError, AttributeError, TypeError, ValueError) as error:
        print("Not ready yet:", error)
