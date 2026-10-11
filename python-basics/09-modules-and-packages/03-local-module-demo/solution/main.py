with open("beacon_rules.py", "w") as module_file:
    module_file.write("def signal_strength(marks):\n    return marks * 5\n")

from beacon_rules import signal_strength
print(signal_strength(3))
