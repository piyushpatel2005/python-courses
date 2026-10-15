from solution import *

def test_register_arrival():
    """Store arrival objects in order and return the count"""
    first = RescueRegister(FeedingService())
    second = RescueRegister(FeedingService())
    bird = Bird("Kite", "meat", 80)
    fish = Fish("Gill", "flakes", "fresh")
    assert first.add(bird) == 1
    assert first.add(fish) == 2
    assert first.add(bird) == 3
    assert first.animals == [bird, fish, bird]
    assert first.animals[0] is bird
    assert second.animals == []
    bird.name = "New Kite"
    assert first.animals[0].name == "New Kite"
