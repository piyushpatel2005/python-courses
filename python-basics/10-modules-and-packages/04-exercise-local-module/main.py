with open("shrine_rules.py", "w") as module_file:
    module_file.write("def seal_count(runes):\n    return (runes + 3) // 4\n")

# Import seal_count here.

def prepare_seals(runes):
    pass

print(prepare_seals(9))
