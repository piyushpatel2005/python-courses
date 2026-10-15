from solution import *


def test_01_substitution_in_a_loop():
    assert ability_messages([]) == [], "Empty input returns an empty list."
    assert ability_messages([Ability("X"), GlideAbility("Y")]) == ["Walk X", "Glide Y"]
    class Compatible:
        def __init__(self, text):
            self.text = text
            self.calls = 0
        def activate(self):
            self.calls += 1
            return self.text
    first, second = Compatible("boat"), Compatible("walk")
    assert ability_messages([second, first, second]) == ["walk", "boat", "walk"]
    assert (first.calls, second.calls) == (1, 2), "Call each entry's interface exactly once."
    assert ability_messages(iter([first])) == ["boat"]
