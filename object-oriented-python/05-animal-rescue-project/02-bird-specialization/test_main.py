from solution import *

def test_bird_record():
    """Extend the inherited record with a wingspan"""
    assert issubclass(Bird, Animal)
    for name, food, span in [("Wren", "insects", 15), ("Ibis", "pellets", 86), ("Chick", "mash", 0)]:
        bird = Bird(name, food, span)
        assert (bird.name, bird.food, bird.wingspan_cm, bird.habitat) == (name, food, span, "aviary")
    calls = []
    original = Animal.__init__
    def tracked(self, name, food):
        calls.append((name, food))
        original(self, name, food)
    Animal.__init__ = tracked
    try:
        Bird("Tern", "fish", 50)
        assert calls == [("Tern", "fish")], "Initialize shared fields through super()"
    finally:
        Animal.__init__ = original
