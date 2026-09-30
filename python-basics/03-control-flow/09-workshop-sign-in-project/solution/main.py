capacity = 2
passes = ""
issued = 0
for ticket in range(1, 7):
    if ticket == 2:
        continue
    passes += f"{ticket} "
    issued += 1
    if issued == capacity:
        break
if issued == capacity:
    status = "Full"
else:
    status = "Open"
print("Passes:", passes)
print("Issued:", issued)
print("Status:", status)
