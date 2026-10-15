class Animal:
    habitat = "land"

    def __init__(self, name, food):
        # TODO: store the two arguments on this animal.
        pass

if __name__ == "__main__":
    animal = Animal("Moss", "hay")
    print("Record:", getattr(animal, "name", "unfinished"), getattr(animal, "food", "unfinished"))
