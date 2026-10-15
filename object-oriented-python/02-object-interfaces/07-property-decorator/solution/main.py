class Member:
    def __init__(self, first, last):
        self.first = first
        self.last = last

    @property
    def display_name(self):
        return f"{self.first} {self.last}"


# Supplied console probe: keep this below your implementation.
if __name__ == "__main__":
    try:
        sample = Member("Ari", "Shah")
        print("Display name:", sample.display_name)
        sample.last = "Patel"
        print("Updated name:", sample.display_name)
    except (NameError, AttributeError, TypeError, ValueError) as error:
        print("Not ready yet:", error)
