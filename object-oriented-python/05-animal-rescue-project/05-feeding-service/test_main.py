from solution import *

def test_meal_label():
    """Format the current record without mutating it"""
    service = FeedingService()
    assert not issubclass(FeedingService, Animal)
    animals = [Animal("Elm", "hay"), Bird("Sky", "grain", 42), Fish("Blue", "flakes", "fresh")]
    for animal in animals:
        before = dict(animal.__dict__)
        assert service.meal(animal) == animal.name + ": " + animal.food
        assert animal.__dict__ == before
    animals[0].food = "leaves"
    assert service.meal(animals[0]) == "Elm: leaves"
