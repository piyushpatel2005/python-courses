from solution import *


def test_automatic_values():
    assert list(PackPhase.__members__) == ["PICK", "WRAP", "SEND"], "Keep the three phase names in the requested order"
    assert [member.value for member in PackPhase] == [1, 2, 3]
    import ast
    import solution
    from pathlib import Path
    source = ast.parse(Path(solution.__file__).read_text())
    cls = next(node for node in source.body if isinstance(node, ast.ClassDef) and node.name == "PackPhase")
    assignments = [node for node in cls.body if isinstance(node, (ast.Assign, ast.AnnAssign))]
    assert len(assignments) == 3
    assert all(isinstance(node.value, ast.Call) and isinstance(node.value.func, ast.Name) and node.value.func.id == "auto" for node in assignments), "Use auto() rather than fixed numbers"
