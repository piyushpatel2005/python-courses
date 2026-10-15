from solution import *


def test_label_property_uses_the_getter():
    prop = vars(GameItem).get("label")
    assert isinstance(prop, property), "Create label with the property function."
    assert prop.fget is GameItem.get_label, "Use the supplied get_label function as the getter."
    first, second = GameItem("lantern"), GameItem("signal horn")
    assert first.label == "LANTERN" and second.label == "SIGNAL HORN"
    first.name = "shield"
    assert first.label == "SHIELD" and second.label == "SIGNAL HORN", "Compute the label from current instance data."
