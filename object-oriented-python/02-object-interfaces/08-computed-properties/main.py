class ToolBatch:
    def __init__(self, total, loaned):
        self.total = total
        self.loaned = loaned

    # Add the computed property here.


# Supplied console probe: keep this below your implementation.
if __name__ == "__main__":
    try:
        sample = ToolBatch(10, 3)
        print("Available:", sample.available)
        sample.loaned = 6
        print("After more loans:", sample.available)
    except (NameError, AttributeError, TypeError, ValueError) as error:
        print("Not ready yet:", error)
