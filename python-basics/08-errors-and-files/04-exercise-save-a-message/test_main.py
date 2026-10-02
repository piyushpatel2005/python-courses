from solution import save_signal, load_signal

def test_save_signal():
    save_signal("Dim")
    save_signal("Bright")
    with open("shrine-save.txt", "r", encoding="utf-8") as file:
        assert file.read() == "Bright"

def test_load_signal():
    with open("shrine-save.txt", "w", encoding="utf-8") as file:
        file.write("Ridge\nCove")
    assert load_signal() == "Ridge\nCove"
