from solution import *


def test_static_normalization_needs_no_receiver():
    assert isinstance(vars(Tool).get("normalize_code"), staticmethod), "Use @staticmethod for a helper with no self or cls."
    instance = Tool()
    for raw, expected in (("  ab-7 ", "AB-7"), ("	tool box\n", "TOOL BOX"), ("", ""), ("X9", "X9")):
        assert Tool.normalize_code(raw) == expected
        assert instance.normalize_code(raw) == expected, "An instance call must not inject self into a static method."
