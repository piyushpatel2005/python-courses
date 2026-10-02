def write_note(text):
    with open("atlas-save.txt", "w") as file:
        file.write(text)


def read_note():
    with open("atlas-save.txt", "r") as file:
        return file.read()


write_note("Follow the silver path")
print("Saved clue:", read_note())
