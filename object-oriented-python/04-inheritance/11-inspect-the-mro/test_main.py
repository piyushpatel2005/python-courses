from solution import *


def test_01_inspect_the_mro():
    assert mro_names(LanternSprite) == ["LanternSprite", "GlowMixin", "TrailMixin", "Entity", "object"]
    assert mro_names(Entity) == ["Entity", "object"]
    assert mro_names(object) == ["object"]
    class Root:
        pass
    class Left(Root):
        pass
    class Right(Root):
        pass
    class Both(Right, Left):
        pass
    assert mro_names(Both) == ["Both", "Right", "Left", "Root", "object"], "Read the provided class's MRO, not a fixed hierarchy."
