def write_note(text):
    with open("workshop-note.txt", "w") as file:
        file.write(text)


def read_note():
    with open("workshop-note.txt", "r") as file:
        return file.read()


write_note("Markers by the entrance")
print("Saved note:", read_note())
