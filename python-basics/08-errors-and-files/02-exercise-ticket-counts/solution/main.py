def ticket_count(text):
    try:
        return int(text)
    except ValueError:
        return 0

def ticket_label(text):
    return f"Tickets: {ticket_count(text)}"

print(ticket_label("3"))
print(ticket_label("many"))
