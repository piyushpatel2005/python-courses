from solution import *


def test_01_cooperative_diamond():
    events = []
    assert Report().build(events) is events
    assert events == ["signed", "dated", "document"], "Each participant must run once in MRO order."
    events = ["start"]
    assert Signed().build(events) is events
    assert events == ["start", "signed", "document"]
    class ReverseReport(Dated, Signed):
        pass
    events = []
    assert ReverseReport().build(events) is events
    assert events == ["dated", "signed", "document"]
    class Extra(Document):
        def build(self, events):
            events.append("extra")
            return super().build(events)
    class Extended(Signed, Extra):
        pass
    events = []
    assert Extended().build(events) is events
    assert events == ["signed", "extra", "document"]
