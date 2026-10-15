from solution import *

def test_animal_record():
    """Store independent animal records"""
    first = Animal("Fern", "leaves")
    second = Animal("Pip", "seeds")
    assert (first.name, first.food) == ("Fern", "leaves")
    assert (second.name, second.food) == ("Pip", "seeds")
    first.name = "Ash"
    assert second.name == "Pip"
    assert Animal("", "").food == ""
