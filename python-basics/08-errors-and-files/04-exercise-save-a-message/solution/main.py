def save_signal(text):
    with open("shrine-save.txt", "w", encoding="utf-8") as file:
        file.write(text)

def load_signal():
    with open("shrine-save.txt", "r", encoding="utf-8") as file:
        return file.read()

save_signal("Beacon restored")
print("Signal:", load_signal())
