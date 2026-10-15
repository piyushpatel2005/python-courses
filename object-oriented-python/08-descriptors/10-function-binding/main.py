def bind_to(function, instance):
    return None

class Player:
    def __init__(self, name):
        self.name = name

def welcome(self, ending):
    return "Welcome " + self.name + ending


if __name__ == "__main__":
    try:
        player = Player("Uma")
        method = bind_to(welcome, player)
        print(method("!"))
    except (AttributeError, TypeError, ValueError, KeyError, NameError) as error:
        print("Not ready:", type(error).__name__, str(error))
