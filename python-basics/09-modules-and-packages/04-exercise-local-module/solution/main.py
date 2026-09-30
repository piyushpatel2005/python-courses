with open("supply_rules.py", "w") as module_file:
    module_file.write("def box_count(items):\n    return (items + 3) // 4\n")

from supply_rules import box_count

def order_boxes(items):
    return box_count(items)

print(order_boxes(9))
