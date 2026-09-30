def save_reminder(text):
    with open("supply-reminder.txt", "w", encoding="utf-8") as file:
        file.write(text)

def load_reminder():
    with open("supply-reminder.txt", "r", encoding="utf-8") as file:
        return file.read()

save_reminder("Bring extra pens")
print("Reminder:", load_reminder())
