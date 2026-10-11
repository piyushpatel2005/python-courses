note = "Light the west beacon"  # Change this text.
with open("shrine-note.txt", "w", encoding="utf-8") as file:
    file.write(note)
with open("shrine-note.txt", "r", encoding="utf-8") as file:
    saved_note = file.read()
print(saved_note)
