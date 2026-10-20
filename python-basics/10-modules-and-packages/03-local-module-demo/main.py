with open("shipping_rules.py", "w", encoding="utf-8") as module_file:
    module_file.write("def shipping_cost(weight):\n    return weight * 5\n")

from shipping_rules import shipping_cost
print(shipping_cost(2))
