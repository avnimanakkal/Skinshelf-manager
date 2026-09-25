from datetime import date, timedelta


def get_status(product, today):
    year, month, day = product["open_date"]
    opened = date(year, month, day)
    expiry_date = opened + timedelta(days=product["shelf_life_months"] * 30)
    days_left = (expiry_date - today).days

    if days_left < 0:
        return "Expired"
    elif days_left <= 30:
        return "Use Soon"
    else:
        return "Fresh"


def show_expiry_status(shelf):
    print("===== EXPIRY STATUS =====")
    today = date.today()
    for product in shelf:
        status = get_status(product, today)
        expiry_date = date(*product["open_date"]) + timedelta(days=product["shelf_life_months"] * 30)
        print(product["name"], "| Expires:", expiry_date, "|", status)
