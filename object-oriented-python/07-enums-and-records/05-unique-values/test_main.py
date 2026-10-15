from solution import *


def test_unique_values():
    from enum import Enum
    import ast
    import solution
    from pathlib import Path
    source = ast.parse(Path(solution.__file__).read_text())
    factory = next(node for node in source.body if isinstance(node, ast.FunctionDef) and node.name == "make_abilities")
    enum_class = next(node for node in factory.body if isinstance(node, ast.ClassDef) and node.name == "AbilityChoice")
    assert any(isinstance(node, ast.Name) and node.id == "unique" for node in enum_class.decorator_list), "Apply @unique to AbilityChoice"
    for a, b in [("blink", "shield"), (4, 9), ((1, 2), (3, 4))]:
        choice = make_abilities(a, b)
        assert issubclass(choice, Enum)
        assert choice.FIRST.value == a and choice.SECOND.value == b
    for value in ["same", 7, (2, 3)]:
        try:
            make_abilities(value, value)
        except ValueError:
            pass
        else:
            assert False, "Equal values must raise ValueError"
