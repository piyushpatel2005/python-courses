loaded = ""
for parcel in range(1, 7):
    if parcel == 2:
        continue
    if parcel == 5:
        break
    loaded += f"Loaded {parcel} | "
print(loaded)
