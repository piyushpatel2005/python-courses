from solution import *


def test_01_substitution_in_a_loop():
    assert dispatch_messages([]) == [], "Empty input returns an empty list."
    assert dispatch_messages([Delivery("X"), BikeDelivery("Y")]) == ["Road X", "Bike Y"]
    class Compatible:
        def __init__(self, text):
            self.text = text
            self.calls = 0
        def dispatch(self):
            self.calls += 1
            return self.text
    first, second = Compatible("boat"), Compatible("walk")
    assert dispatch_messages([second, first, second]) == ["walk", "boat", "walk"]
    assert (first.calls, second.calls) == (1, 2), "Call each entry's interface exactly once."
    assert dispatch_messages(iter([first])) == ["boat"]
