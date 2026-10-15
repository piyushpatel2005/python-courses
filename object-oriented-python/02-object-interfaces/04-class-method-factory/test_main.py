from solution import *


def test_class_factory_parses_and_constructs():
    assert isinstance(vars(GameItem).get("from_text"), classmethod), "Decorate from_text with @classmethod."
    for text, name, uses in (("lantern:8", "lantern", 8), ("signal horn:0", "signal horn", 0), ("shield:23", "shield", 23)):
        item = GameItem.from_text(text)
        assert isinstance(item, GameItem) and item.name == name and item.uses == uses
        assert type(item.uses) is int, "Convert the count from text to int."
    calls = []
    marker = object()
    def factory(name, uses):
        calls.append((name, uses))
        return marker
    implementation = vars(GameItem)["from_text"].__func__
    assert implementation(factory, "flute:4") is marker, "Construct through the cls parameter."
    assert calls == [("flute", 4)]
    assert GameItem.from_text("lantern:8") is not GameItem.from_text("lantern:8")
