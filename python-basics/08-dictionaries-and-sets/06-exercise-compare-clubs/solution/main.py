morning_sign_ins = ["Maya", "Luis", "Maya", "Ava"]
afternoon_sign_ins = ["Luis", "Nia"]
morning_attendees = set(morning_sign_ins)
both_sessions = morning_attendees & set(afternoon_sign_ins)
morning_only = morning_attendees - set(afternoon_sign_ins)
print(sorted(morning_attendees), sorted(both_sessions), sorted(morning_only))
