class Animal:
    habitat = "land"

    def __init__(self, name, food):
        self.name = name
        self.food = food

    def move(self):
        return "walk"


class Bird(Animal):
    habitat = "aviary"

    def __init__(self, name, food, wingspan_cm):
        super().__init__(name, food)
        self.wingspan_cm = wingspan_cm

    def move(self):
        return "fly"


class Fish(Animal):
    habitat = "tank"

    def __init__(self, name, food, water_type):
        super().__init__(name, food)
        self.water_type = water_type

    def move(self):
        return "swim"


class FeedingService:
    def meal(self, animal):
        return f"{animal.name}: {animal.food}"


class RescueRegister:
    def __init__(self, feeder):
        self.feeder = feeder
        self.animals = []

    def add(self, animal):
        # TODO: append this animal and return the register's new size.
        pass

if __name__ == "__main__":
    animal = Animal("Moss", "hay")
    print("Record:", getattr(animal, "name", "unfinished"), getattr(animal, "food", "unfinished"))

    bird = Bird("Lark", "seeds", 24)
    print("Bird:", getattr(bird, "name", "unfinished"), getattr(bird, "wingspan_cm", "unfinished"), bird.habitat)

    fish = Fish("Ripple", "flakes", "fresh")
    print("Fish:", getattr(fish, "name", "unfinished"), getattr(fish, "water_type", "unfinished"), fish.habitat)

    print("Movements:", [item.move() for item in [Animal("Moss", "hay"), Bird("Lark", "seeds", 24), Fish("Ripple", "flakes", "fresh")]])

    feeder = FeedingService()
    print("Meal:", feeder.meal(Bird("Lark", "seeds", 24)))

    register = RescueRegister(FeedingService())
    print("Registered:", register.add(Bird("Lark", "seeds", 24)))
