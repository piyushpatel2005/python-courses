seats_left = 2
seat_message = "Not set"

if seats_left == 0:
    seat_message = "Sold out"
elif seats_left < 4:
    seat_message = "Few seats left"
else:
    seat_message = "Seats available"
print(seat_message)
