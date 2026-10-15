from solution import *

def test_daily_care_report():
    """Compose a report from the stored service and animal behaviors"""
    register = RescueRegister(FeedingService())
    assert register.daily_report() == "No animals registered."
    fish = Fish("Fin", "flakes", "salt")
    bird = Bird("Wing", "seeds", 22)
    register.add(fish)
    register.add(bird)
    assert register.daily_report() == "Fin: flakes | tank | swim\nWing: seeds | aviary | fly"
    calls = []
    class CustomFeeder:
        def meal(self, animal):
            calls.append(animal)
            return "Meal for " + animal.name
    class Visitor(Animal):
        habitat = "pool"
        def move(self):
            return "paddle"
    visitor = Visitor("Otto", "fish")
    custom = RescueRegister(CustomFeeder())
    custom.add(visitor)
    custom.add(visitor)
    assert custom.daily_report() == "Meal for Otto | pool | paddle\nMeal for Otto | pool | paddle"
    assert calls == [visitor, visitor]
    assert custom.animals == [visitor, visitor]
