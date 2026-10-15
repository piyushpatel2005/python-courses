from solution import *

def test_fish_record():
    """Extend the inherited record with water conditions"""
    assert issubclass(Fish, Animal)
    for name, food, water in [("Fin", "flakes", "fresh"), ("Coral", "shrimp", "salt"), ("Reed", "algae", "brackish")]:
        fish = Fish(name, food, water)
        assert (fish.name, fish.food, fish.water_type, fish.habitat) == (name, food, water, "tank")
    calls = []
    original = Animal.__init__
    def tracked(self, name, food):
        calls.append((name, food))
        original(self, name, food)
    Animal.__init__ = tracked
    try:
        Fish("Dot", "flakes", "fresh")
        assert calls == [("Dot", "flakes")], "Initialize shared fields through super()"
    finally:
        Animal.__init__ = original
