import ast
import inspect
import solution
from solution import is_invoice

def test_package_import():
    """Import ElementTree as ET."""
    tree = ast.parse(inspect.getsource(solution))
    assert any(
        isinstance(node, ast.Import)
        and any(alias.name == "xml.etree.ElementTree" and alias.asname == "ET"
                for alias in node.names)
        for node in tree.body
    ), "Import xml.etree.ElementTree as ET."

def test_is_invoice():
    """Compare the parsed outer tag, not an inner tag."""
    assert is_invoice("<invoice><line /></invoice>") is True
    assert is_invoice("<order><invoice /></order>") is False
    assert is_invoice("<invoice />") is True
    original = solution.ET.fromstring
    calls = []
    def tracked(xml_text):
        calls.append(xml_text)
        return original(xml_text)
    try:
        solution.ET.fromstring = tracked
        assert is_invoice("<other />") is False
        assert calls == ["<other />"], "Parse the supplied XML with ET.fromstring."
    finally:
        solution.ET.fromstring = original
