from solution import *


def test_unique_values():
    from enum import Enum
    import ast
    import solution
    from pathlib import Path
    source = ast.parse(Path(solution.__file__).read_text())
    factory = next(node for node in source.body if isinstance(node, ast.FunctionDef) and node.name == "make_choices")
    enum_class = next(node for node in factory.body if isinstance(node, ast.ClassDef) and node.name == "Choice")
    assert any(isinstance(node, ast.Name) and node.id == "unique" for node in enum_class.decorator_list), "Apply @unique to Choice"
    for a, b in [("red", "blue"), (4, 9), ((1, 2), (3, 4))]:
        choice = make_choices(a, b)
        assert issubclass(choice, Enum)
        assert choice.FIRST.value == a and choice.SECOND.value == b
    for value in ["same", 7, (2, 3)]:
        try:
            make_choices(value, value)
        except ValueError:
            pass
        else:
            assert False, "Equal values must raise ValueError"
