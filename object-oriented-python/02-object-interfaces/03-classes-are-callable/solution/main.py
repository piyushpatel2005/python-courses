class Tool:
    def __init__(self, name):
        self.name = name

class Member:
    def __init__(self, name):
        self.name = name

def create_record(factory, name):
    return factory(name)


# Supplied console probe: keep this below your implementation.
if __name__ == "__main__":
    try:
        print("Tool:", create_record(Tool, "drill").name)
        print("Member:", create_record(Member, "Ari").name)
    except (NameError, AttributeError, TypeError, ValueError) as error:
        print("Not ready yet:", error)
