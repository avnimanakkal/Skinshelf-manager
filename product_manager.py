import validators


def add_product(shelf):
    name = validators.get_text("Product name: ")
    category = validators.get_text("Category: ")
    price = validators.get_number("Price: ")
    months = validators.get_whole_number("Shelf life in months: ", 1, 60)
    day = validators.get_whole_number("Opened on - day: ", 1, 31)
    month = validators.get_whole_number("Opened on - month: ", 1, 12)
    year = validators.get_whole_number("Opened on - year: ", 2020, 2030)
    text = input("Key actives (comma separated): ")

    actives = set()
    for a in text.split(","):
        cleaned = a.strip().lower()
        if cleaned != "":
            actives.add(cleaned)

    shelf.append({
        "name": name,
        "category": category,
        "price": price,
        "shelf_life_months": months,
        "open_date": (year, month, day),
        "actives": actives
    })
    print("Added!")


def view_shelf(shelf):
    if len(shelf) == 0:
        print("Your shelf is empty.")
        return

    print("===== YOUR SHELF =====")
    number = 1
    for product in shelf:
        print(str(number) + ".", product["name"], "-", product["category"], "- Rs", product["price"])
        number = number + 1


def edit_product(shelf):
    view_shelf(shelf)
    if len(shelf) == 0:
        return

    index = validators.get_whole_number("Enter product number to edit: ", 1, len(shelf))
    product = shelf[index - 1]

    print("Leave blank to keep the current value.")
    new_price = input("New price (current " + str(product["price"]) + "): ")
    if new_price.strip() != "":
        try:
            product["price"] = float(new_price)
        except ValueError:
            print("Invalid price, keeping the old one.")

    print("Updated!")


def delete_product(shelf):
    view_shelf(shelf)
    if len(shelf) == 0:
        return

    index = validators.get_whole_number("Enter product number to delete: ", 1, len(shelf))
    removed = shelf.pop(index - 1)
    print("Deleted:", removed["name"])

