import ast
import inspect
import textwrap
from solution import ticket_count, ticket_label

def test_ticket_count():
    assert ticket_count("5") == 5
    assert ticket_count("many") == 0
    tree = ast.parse(textwrap.dedent(inspect.getsource(ticket_count)))
    assert any(isinstance(n, ast.ExceptHandler) and isinstance(n.type, ast.Name) and n.type.id == "ValueError" for n in ast.walk(tree)), "Catch the specific ValueError."

def test_ticket_label():
    assert ticket_label("2") == "Tickets: 2"
    assert ticket_label("broken") == "Tickets: 0"
