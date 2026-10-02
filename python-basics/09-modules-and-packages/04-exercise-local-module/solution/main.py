with open("shrine_rules.py", "w") as module_file:
    module_file.write("def seal_count(runes):\n    return (runes + 3) // 4\n")

from shrine_rules import seal_count

def prepare_seals(runes):
    return seal_count(runes)

print(prepare_seals(9))
