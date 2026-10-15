from solution import *


def test_label_uses_receiver_attribute_lookup():
    first, second = AssetLabel("A4"), AssetLabel("B9")
    assert first.text() == "TOOL-A4", "Read prefix through self, not the global name."
    first.prefix = "REPAIR"
    assert first.text() == "REPAIR-A4" and second.text() == "TOOL-B9"
    original = AssetLabel.prefix
    try:
        AssetLabel.prefix = "LOAN"
        assert second.text() == "LOAN-B9" and first.text() == "REPAIR-A4"
        second.code = "C2"
        assert second.text() == "LOAN-C2"
    finally:
        AssetLabel.prefix = original
