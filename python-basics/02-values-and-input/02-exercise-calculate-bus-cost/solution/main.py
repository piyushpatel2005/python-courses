points_per_cache = 3
caches = 7
pack_slots = 25
energy_per_point = 4
energy_cost = points_per_cache * caches * energy_per_point
open_slots = pack_slots - points_per_cache * caches
print("Energy cost:", energy_cost)
print("Open slots:", open_slots)
