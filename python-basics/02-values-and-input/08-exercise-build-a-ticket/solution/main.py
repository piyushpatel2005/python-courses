visitor_text = "Maya"
tickets_text = "3"
unit_cost = 6.0
ticket_count = int(tickets_text)
total_cost = ticket_count * unit_cost
ticket_line = f"Ticket for {visitor_text}: {ticket_count} seats, ${total_cost:.2f}"
print("Count:", ticket_count)
print("Total:", total_cost)
print(ticket_line)
