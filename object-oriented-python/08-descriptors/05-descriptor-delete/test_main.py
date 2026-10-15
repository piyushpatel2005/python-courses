from solution import *


def test_descriptor_delete():
    first, second = Draft(), Draft()
    first.label, second.label = "remove", "retain"
    first.note = "Keep unrelated data"
    del first.label
    assert first.note == "Keep unrelated data"
    assert first.label is None and second.label == "retain"
    assert Draft.label.key not in first.__dict__
    del first.label
    first.label = "new"
    assert first.label == "new"
    assert isinstance(Draft.label, CachedLabel)
