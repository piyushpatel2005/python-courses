with open("route_rules.py", "w") as module_file:
    module_file.write("def travel_minutes(stops):\n    return stops * 5\n")

from route_rules import travel_minutes
print(travel_minutes(3))
