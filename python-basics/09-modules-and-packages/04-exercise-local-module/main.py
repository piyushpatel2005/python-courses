with open("supply_rules.py", "w") as module_file:
    module_file.write("def box_count(items):\n    return (items + 3) // 4\n")

# Import box_count here.

def order_boxes(items):
    pass

print(order_boxes(9))
