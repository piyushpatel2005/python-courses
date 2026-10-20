note = "Order being packed"  # Change this text.
with open("pickup-note.txt", "w", encoding="utf-8") as file:
    file.write(note)
with open("pickup-note.txt", "r", encoding="utf-8") as file:
    saved_note = file.read()
print(saved_note)
