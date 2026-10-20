flour_bags = 6
milk_cartons = 1
store_closed = True
enough_flour = flour_bags >= 4
can_take_order = enough_flour and milk_cartons >= 1
needs_restock = flour_bags < 4 or milk_cartons == 0
store_open = not store_closed
print(enough_flour)
print(can_take_order)
print(needs_restock)
print(store_open)
