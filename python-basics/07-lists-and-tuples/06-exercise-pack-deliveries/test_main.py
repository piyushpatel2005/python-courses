from solution import *
import ast
import contextlib
import io
import solution


def _tree():
    with open(solution.__file__, encoding="utf-8") as file:
        return ast.parse(file.read())


def _assignment(name):
    for node in _tree().body:
        if isinstance(node, ast.Assign) and any(isinstance(t, ast.Name) and t.id == name for t in node.targets):
            return node.value
    return None


def indexed(name, source):
    value = _assignment(name)
    return isinstance(value, ast.Subscript) and isinstance(value.value, ast.Name) and value.value.id == source


def sliced(name, source):
    value = _assignment(name)
    return indexed(name, source) and isinstance(value.slice, ast.Slice)


def list_literal(name):
    return isinstance(_assignment(name), ast.List)


def unpacked(names, source):
    return any(isinstance(node, ast.Assign) and len(node.targets) == 1
               and isinstance(node.targets[0], ast.Tuple)
               and [e.id for e in node.targets[0].elts if isinstance(e, ast.Name)] == list(names)
               and isinstance(node.value, ast.Name) and node.value.id == source
               for node in _tree().body)


def index_write(name, index):
    return any(isinstance(node, ast.Assign) and any(isinstance(t, ast.Subscript)
               and isinstance(t.value, ast.Name) and t.value.id == name
               and isinstance(t.slice, ast.Constant) and t.slice.value == index
               for t in node.targets) for node in _tree().body)


def calls(name, method):
    return any(isinstance(node, ast.Call) and isinstance(node.func, ast.Attribute)
               and isinstance(node.func.value, ast.Name) and node.func.value.id == name
               and node.func.attr == method for node in ast.walk(_tree()))


def get_with_default(target, source, key, fallback):
    value = _assignment(target)
    return isinstance(value, ast.Call) and isinstance(value.func, ast.Attribute) and isinstance(value.func.value, ast.Name) and value.func.value.id == source and value.func.attr == "get" and len(value.args) == 2 and all(isinstance(arg, ast.Constant) and arg.value == expected for arg, expected in zip(value.args, [key, fallback]))


def loop_appends(name):
    return any(isinstance(node, ast.For) and any(isinstance(part, ast.Call)
               and isinstance(part.func, ast.Attribute) and isinstance(part.func.value, ast.Name)
               and part.func.value.id == name and part.func.attr == "append"
               for statement in node.body for part in ast.walk(statement)) for node in _tree().body)


def loop_method(method, name):
    return any(isinstance(node, ast.For) and isinstance(node.iter, ast.Call)
               and isinstance(node.iter.func, ast.Attribute) and node.iter.func.attr == method
               and any(isinstance(part, ast.Name) and part.id == name
                       for statement in node.body for part in ast.walk(statement)) for node in _tree().body)


def set_from(name, source):
    value = _assignment(name)
    return isinstance(value, ast.Call) and isinstance(value.func, ast.Name) and value.func.id == "set" and len(value.args) == 1 and isinstance(value.args[0], ast.Name) and value.args[0].id == source


def set_op(name, operator):
    value = _assignment(name)
    return isinstance(value, ast.BinOp) and type(value.op).__name__ == operator


def fstring(name):
    return isinstance(_assignment(name), ast.JoinedStr)


def _variant():
    tree = _tree()
    replacements = VARIANTS
    for node in tree.body:
        if isinstance(node, ast.Assign) and len(node.targets) == 1 and isinstance(node.targets[0], ast.Name):
            name = node.targets[0].id
            if name in replacements:
                node.value = ast.parse(repr(replacements[name]), mode="eval").body
    ast.fix_missing_locations(tree)
    result = {}
    with contextlib.redirect_stdout(io.StringIO()):
        exec(compile(tree, "changed_fixture.py", "exec"), result)
    return result

VARIANTS = {'orders': ['order 205', 'order 206', 'order 207', 'order 208']}

def test_01():
    """Check task 1 with the supplied and changed data."""
    assert today == ["order 101", "order 102", "order 103"], "Check task 1 with the supplied data."
    assert sliced("today", "orders"), "Use the requested collection operation in task 1."
    changed = _variant()
    assert eval('today == ["order 205", "order 206", "order 207"]', changed), "Check task 1 with different data."

def test_02():
    """Check task 2 with the supplied and changed data."""
    assert labels == ["Pack order 101", "Pack order 102", "Pack order 103"], "Check task 2 with the supplied data."
    assert loop_appends("labels"), "Use the requested collection operation in task 2."
    changed = _variant()
    assert eval('labels == ["Pack order 205", "Pack order 206", "Pack order 207"]', changed), "Check task 2 with different data."
