capacity = 3
admitted = ""
count = 0
for visitor in range(1, 9):
    if visitor == 3:
        continue
    admitted += f"{visitor} "
    count += 1
    if count == capacity:
        break
print(admitted)
print(count)
