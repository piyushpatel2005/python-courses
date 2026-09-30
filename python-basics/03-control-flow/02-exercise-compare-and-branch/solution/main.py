copies_left = 2
low_stock = copies_left < 3
if copies_left == 0:
    sign = "Unavailable"
elif low_stock:
    sign = "Almost gone"
else:
    sign = "Available"
print(low_stock)
print(sign)
