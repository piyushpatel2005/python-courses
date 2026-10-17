coins_per_chest = 3
chests = 7
pack_slots = 25
points_per_coin = 4
points_needed = coins_per_chest * chests * points_per_coin
open_slots = pack_slots - coins_per_chest * chests
print("Points needed:", points_needed)
print("Open slots:", open_slots)
