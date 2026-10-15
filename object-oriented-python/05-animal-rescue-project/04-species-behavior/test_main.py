from solution import *

def test_species_movement():
    """Dispatch movement through each animal object"""
    animals = [Fish("A", "f", "salt"), Animal("B", "g"), Bird("C", "h", 30), Bird("D", "i", 10)]
    assert [animal.move() for animal in animals] == ["swim", "walk", "fly", "fly"]
    class YoungBird(Bird):
        pass
    assert YoungBird("E", "j", 0).move() == "fly"
