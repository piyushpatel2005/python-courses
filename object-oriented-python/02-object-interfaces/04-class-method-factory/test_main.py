from solution import *


def test_class_factory_parses_and_constructs():
    assert isinstance(vars(Tool).get("from_text"), classmethod), "Decorate from_text with @classmethod."
    for text, name, uses in (("drill:8", "drill", 8), ("hand plane:0", "hand plane", 0), ("saw:23", "saw", 23)):
        item = Tool.from_text(text)
        assert isinstance(item, Tool) and item.name == name and item.uses == uses
        assert type(item.uses) is int, "Convert the count from text to int."
    calls = []
    marker = object()
    def factory(name, uses):
        calls.append((name, uses))
        return marker
    implementation = vars(Tool)["from_text"].__func__
    assert implementation(factory, "vice:4") is marker, "Construct through the cls parameter."
    assert calls == [("vice", 4)]
    assert Tool.from_text("drill:8") is not Tool.from_text("drill:8")
