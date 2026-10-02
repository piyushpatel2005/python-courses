raw_notice = "  BEACON DIM  "
notice = raw_notice.strip().lower()
lit_notice = notice.replace("dim", "lit")
is_beacon_notice = notice.startswith("beacon")
print(notice, lit_notice, is_beacon_notice)
