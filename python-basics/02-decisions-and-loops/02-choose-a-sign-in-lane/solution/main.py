seats_left = 2
if seats_left == 0:
    lane = "Waitlist"
elif seats_left < 4:
    lane = "Last seats"
else:
    lane = "Open"
print(lane)
