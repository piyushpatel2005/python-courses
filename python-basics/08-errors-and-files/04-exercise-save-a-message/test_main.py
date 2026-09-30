from solution import save_reminder, load_reminder

def test_save_reminder():
    save_reminder("First")
    save_reminder("Second")
    with open("supply-reminder.txt", "r", encoding="utf-8") as file:
        assert file.read() == "Second"

def test_load_reminder():
    with open("supply-reminder.txt", "w", encoding="utf-8") as file:
        file.write("Pens\nPaper")
    assert load_reminder() == "Pens\nPaper"
