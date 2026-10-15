from solution import *


def test_01_cooperative_diamond():
    events = []
    assert LanternSprite().build(events) is events
    assert events == ["glow", "trail", "entity"], "Each participant must run once in MRO order."
    events = ["start"]
    assert GlowMixin().build(events) is events
    assert events == ["start", "glow", "entity"]
    class ReverseSprite(TrailMixin, GlowMixin):
        pass
    events = []
    assert ReverseSprite().build(events) is events
    assert events == ["trail", "glow", "entity"]
    class Extra(Entity):
        def build(self, events):
            events.append("extra")
            return super().build(events)
    class Extended(GlowMixin, Extra):
        pass
    events = []
    assert Extended().build(events) is events
    assert events == ["glow", "extra", "entity"]
