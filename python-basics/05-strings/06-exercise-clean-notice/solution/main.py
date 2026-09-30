raw_notice = "  HALL CLOSED  "
notice = raw_notice.strip().lower()
open_notice = notice.replace("closed", "open")
is_hall_notice = notice.startswith("hall")
print(notice, open_notice, is_hall_notice)
