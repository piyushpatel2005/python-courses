from solution import *


def test_label_property_uses_the_getter():
    prop = vars(Tool).get("label")
    assert isinstance(prop, property), "Create label with the property function."
    assert prop.fget is Tool.get_label, "Use the supplied get_label function as the getter."
    first, second = Tool("drill"), Tool("hand plane")
    assert first.label == "DRILL" and second.label == "HAND PLANE"
    first.name = "saw"
    assert first.label == "SAW" and second.label == "HAND PLANE", "Compute the label from current instance data."
