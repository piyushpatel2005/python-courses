from solution import *


def test_dataclass_enum_values():
    assert [m.name for m in PaperSize] == ["CARD", "POSTER"]
    for member, width, height in [(PaperSize.CARD, 10, 15), (PaperSize.POSTER, 30, 40)]:
        assert isinstance(member.value, Dimensions)
        assert (member.value.width, member.value.height) == (width, height)
    assert PaperSize(Dimensions(10, 15)) is PaperSize.CARD
    assert PaperSize.CARD is not PaperSize.POSTER
