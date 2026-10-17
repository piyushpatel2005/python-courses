ari_stops = ["Ridge", "Cove", "Ridge", "Grove"]
scout_stops = ["Cove", "Basin"]
ari_route = set(ari_stops)
overlap = ari_route & set(scout_stops)
ari_only = ari_route - set(scout_stops)
print(sorted(ari_route), sorted(overlap), sorted(ari_only))
