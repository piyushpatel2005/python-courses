from solution import *


def test_static_normalization_needs_no_receiver():
    assert isinstance(vars(GameItem).get("normalize_code"), staticmethod), "Use @staticmethod for a helper with no self or cls."
    instance = GameItem()
    for raw, expected in (("  ab-7 ", "AB-7"), ("	item pouch\n", "ITEM POUCH"), ("", ""), ("X9", "X9")):
        assert GameItem.normalize_code(raw) == expected
        assert instance.normalize_code(raw) == expected, "An instance call must not inject self into a static method."
