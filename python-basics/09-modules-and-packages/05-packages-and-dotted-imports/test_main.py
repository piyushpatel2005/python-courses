import ast
import inspect
import solution
from solution import tag_name

def test_package_call():
    """The package module parses the new tag"""
    assert tag_name("<beacon />") == "beacon"
    tree = ast.parse(inspect.getsource(solution))
    assert any(
        isinstance(node, ast.Expr) and isinstance(node.value, ast.Call)
        and isinstance(node.value.func, ast.Name) and node.value.func.id == "print"
        and len(node.value.args) == 1
        and isinstance(node.value.args[0], ast.Call)
        and isinstance(node.value.args[0].func, ast.Name)
        and node.value.args[0].func.id == "tag_name"
        and len(node.value.args[0].args) == 1
        and isinstance(node.value.args[0].args[0], ast.Constant)
        and node.value.args[0].args[0].value == "<beacon />"
        and eval(compile(ast.Expression(node.value.args[0]), "<package call>", "eval"), {"tag_name": tag_name}) == "beacon"
        for node in tree.body
    ), "Print the result of tag_name('<beacon />'), not a comment or literal."
