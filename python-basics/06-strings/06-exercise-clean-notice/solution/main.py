raw_notice = "  SHOP CLOSED  "
notice = raw_notice.strip().lower()
updated_notice = notice.replace("closed", "open")
is_shop_notice = notice.startswith("shop")
print(notice, updated_notice, is_shop_notice)
