from solution import save_message, load_message

def test_save_message():
    """Writing again replaces the earlier message."""
    save_message("Call at noon")
    save_message("Call at three")
    with open("message.txt", "r", encoding="utf-8") as file:
        assert file.read() == "Call at three"

def test_load_message():
    """Read the whole saved message."""
    with open("message.txt", "w", encoding="utf-8") as file:
        file.write("Leave at desk\nAsk for Sam")
    assert load_message() == "Leave at desk\nAsk for Sam"
