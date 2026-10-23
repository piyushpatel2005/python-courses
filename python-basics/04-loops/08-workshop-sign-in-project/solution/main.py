capacity = 2
checked_in = ""
attendee_count = 0
for registration_id in range(1, 7):
    if registration_id == 2:
        continue
    checked_in += f"{registration_id} "
    attendee_count += 1
    if attendee_count == capacity:
        break
if attendee_count == capacity:
    status = "Full"
else:
    status = "Spaces left"
print("Checked in:", checked_in)
print("Attendees:", attendee_count)
print("Status:", status)
