def show_spending_report(shelf):
    totals = {}

    for product in shelf:
        category = product["category"]
        if category in totals:
            totals[category] = totals[category] + product["price"]
        else:
            totals[category] = product["price"]

    print("===== SPENDING REPORT =====")
    grand_total = 0
    top_category = ""
    top_amount = 0

    for category in totals:
        amount = totals[category]
        print(category, ": Rs", amount)
        grand_total = grand_total + amount
        if amount > top_amount:
            top_amount = amount
            top_category = category

    print("-------------------------")
    print("Total spent: Rs", grand_total)
    if top_category != "":
        print("Most spent on:", top_category, "(Rs", top_amount, ")")
