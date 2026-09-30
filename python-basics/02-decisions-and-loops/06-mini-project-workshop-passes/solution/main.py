capacity = 3
passes = ""
issued = 0
for ticket in range(1, 8):
    if ticket == 3:
        continue
    passes += f"{ticket} "
    issued += 1
    if issued == capacity:
        break
if issued == capacity:
    desk_status = "Full"
else:
    desk_status = "Open"
print(passes)
print(desk_status)
