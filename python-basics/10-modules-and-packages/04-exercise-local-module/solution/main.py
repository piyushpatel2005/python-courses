with open("tax_rules.py", "w", encoding="utf-8") as module_file:
    module_file.write("def sales_tax(subtotal):\n    return subtotal * 0.10\n")

from tax_rules import sales_tax

def tax_for_order(subtotal):
    return sales_tax(subtotal)

print(tax_for_order(40))
