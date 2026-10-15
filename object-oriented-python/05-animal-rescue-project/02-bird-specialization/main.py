class Animal:
    habitat = "land"

    def __init__(self, name, food):
        self.name = name
        self.food = food


class Bird(Animal):
    habitat = "aviary"

    def __init__(self, name, food, wingspan_cm):
        # TODO: initialize the inherited record and the wingspan.
        pass

if __name__ == "__main__":
    animal = Animal("Moss", "hay")
    print("Record:", getattr(animal, "name", "unfinished"), getattr(animal, "food", "unfinished"))

    bird = Bird("Lark", "seeds", 24)
    print("Bird:", getattr(bird, "name", "unfinished"), getattr(bird, "wingspan_cm", "unfinished"), bird.habitat)
