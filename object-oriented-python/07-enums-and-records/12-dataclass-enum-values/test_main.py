from solution import *


def test_dataclass_enum_values():
    assert [m.name for m in SpriteSize] == ["WISP", "GOLEM"]
    for member, width, height in [(SpriteSize.WISP, 10, 15), (SpriteSize.GOLEM, 30, 40)]:
        assert isinstance(member.value, Dimensions)
        assert (member.value.width, member.value.height) == (width, height)
    assert SpriteSize(Dimensions(10, 15)) is SpriteSize.WISP
    assert SpriteSize.WISP is not SpriteSize.GOLEM
    from dataclasses import FrozenInstanceError
    try:
        SpriteSize.WISP.value.width = 99
    except FrozenInstanceError:
        pass
    else:
        assert False, "Keep the supplied dimensions record frozen"
    assert SpriteSize.WISP.value.width == 10
