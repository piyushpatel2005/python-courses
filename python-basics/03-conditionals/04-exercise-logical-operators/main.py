flour_bags = 6
milk_cartons = 1
store_closed = True
enough_flour = flour_bags >= 4
can_take_order = False  # Require both enough_flour and at least one carton.
needs_restock = True  # Check for either item needs restocking.
store_open = True  # Reverse store_closed.
print(enough_flour)
print(can_take_order)
print(needs_restock)
print(store_open)
