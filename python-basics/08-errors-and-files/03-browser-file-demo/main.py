note = "Check the south door"  # Change this text.
with open("shift-note.txt", "w", encoding="utf-8") as file:
    file.write(note)
with open("shift-note.txt", "r", encoding="utf-8") as file:
    saved_note = file.read()
print(saved_note)
