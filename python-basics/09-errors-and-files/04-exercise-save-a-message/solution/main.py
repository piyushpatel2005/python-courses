def save_message(text):
    with open("message.txt", "w", encoding="utf-8") as file:
        file.write(text)

def load_message():
    with open("message.txt", "r", encoding="utf-8") as file:
        return file.read()

save_message("Please call before delivery")
print("Message:", load_message())
