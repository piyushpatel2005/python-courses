required = 3
marks = ""
collected = 0
for rune in range(1, 8):
    if rune == 3:
        continue
    marks += f"{rune} "
    collected += 1
    if collected == required:
        break
if collected == required:
    gate_status = "Unlocked"
else:
    gate_status = "Sealed"
print(marks)
print(gate_status)
