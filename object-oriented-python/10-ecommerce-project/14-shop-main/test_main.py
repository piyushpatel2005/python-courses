from solution import *


def test_behavior():
    """Launch the console shop."""
    import io
    from contextlib import redirect_stdout
    for unused in range(2):
        output = io.StringIO()
        with redirect_stdout(output):
            responses = main(["add TEA 3", "checkout", "show O1"])
        assert responses == ["Added TEA x 3", "Created O1", "Order O1\nTEA | Tea | 3 x | $17.25\nTotal: $17.25"]
        assert output.getvalue() == "\n".join(responses) + "\n"
    output = io.StringIO()
    with redirect_stdout(output):
        assert main([]) == []
    assert output.getvalue() == ""
    with redirect_stdout(io.StringIO()):
        defaults = main()
    assert "Created O1" in defaults and "O1: shipped" in defaults
    assert defaults[-1] == "Order O1\nMUG | Mug | 2 x | $25.00\nTotal: $25.00"
