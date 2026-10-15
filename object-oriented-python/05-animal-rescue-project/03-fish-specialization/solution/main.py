class Animal:
    habitat = "land"

    def __init__(self, name, food):
        self.name = name
        self.food = food


class Bird(Animal):
    habitat = "aviary"

    def __init__(self, name, food, wingspan_cm):
        super().__init__(name, food)
        self.wingspan_cm = wingspan_cm


class Fish(Animal):
    habitat = "tank"

    def __init__(self, name, food, water_type):
        super().__init__(name, food)
        self.water_type = water_type

if __name__ == "__main__":
    animal = Animal("Moss", "hay")
    print("Record:", getattr(animal, "name", "unfinished"), getattr(animal, "food", "unfinished"))

    bird = Bird("Lark", "seeds", 24)
    print("Bird:", getattr(bird, "name", "unfinished"), getattr(bird, "wingspan_cm", "unfinished"), bird.habitat)

    fish = Fish("Ripple", "flakes", "fresh")
    print("Fish:", getattr(fish, "name", "unfinished"), getattr(fish, "water_type", "unfinished"), fish.habitat)
