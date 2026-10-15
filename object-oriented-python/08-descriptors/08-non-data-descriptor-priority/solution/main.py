class Greeting:
    def __get__(self, instance, owner):
        if instance is None:
            return self
        return "Hello, " + instance.name

class Profile:
    greeting = Greeting()

    def __init__(self, name):
        self.name = name


if __name__ == "__main__":
    try:
        first, second = Profile("Mina"), Profile("Oren")
        print(first.greeting)
        first.greeting = "Welcome back"
        print(first.greeting, second.greeting)
    except (AttributeError, TypeError, ValueError, KeyError, NameError) as error:
        print("Not ready:", type(error).__name__, str(error))
