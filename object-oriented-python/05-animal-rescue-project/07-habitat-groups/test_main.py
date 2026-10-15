from solution import *

def test_habitat_groups():
    """Return fresh groups in arrival order"""
    register = RescueRegister(FeedingService())
    assert register.habitat_groups() == {}
    class Otter(Animal):
        habitat = "pool"
    a = Bird("One", "seed", 12)
    b = Bird("Two", "seed", 14)
    c = Otter("Three", "fish")
    for animal in [a, c, b, a]:
        register.add(animal)
    grouped = register.habitat_groups()
    assert grouped is not register.habitat_groups(), "Return a new dictionary each time"
    assert grouped == {"aviary": [a, b, a], "pool": [c]}
    assert grouped["aviary"][0] is a
    grouped["aviary"].clear()
    assert register.animals == [a, c, b, a]
    assert register.habitat_groups()["aviary"] == [a, b, a]
