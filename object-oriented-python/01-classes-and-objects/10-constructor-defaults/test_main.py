from solution import *


def test_default_and_explicit_usage_counts():
    new = Tool("new drill")
    assert new.uses == 0 and new.name == "new drill", "An omitted uses argument should default to zero."
    assert Tool("saw", 12).uses == 12
    assert Tool(name="plane", uses=5).uses == 5
    new.uses = 99
    assert Tool("another").uses == 0, "Each new tool starts with its own count."
