with open("tax_rules.py", "w", encoding="utf-8") as module_file:
    module_file.write("def sales_tax(subtotal):\n    return subtotal * 0.10\n")

# Import sales_tax here.

def tax_for_order(subtotal):
    pass

print(tax_for_order(40))
