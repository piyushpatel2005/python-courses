from solution import *


def test_label_uses_receiver_attribute_lookup():
    first, second = ItemLabel("A4"), ItemLabel("B9")
    assert first.text() == "ITEM-A4", "Read prefix through self, not the global name."
    first.prefix = "RARE"
    assert first.text() == "RARE-A4" and second.text() == "ITEM-B9"
    original = ItemLabel.prefix
    try:
        ItemLabel.prefix = "QUEST"
        assert second.text() == "QUEST-B9" and first.text() == "RARE-A4"
        second.code = "C2"
        assert second.text() == "QUEST-C2"
    finally:
        ItemLabel.prefix = original
