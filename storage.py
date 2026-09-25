import json


def save_shelf(shelf):
    data = []
    for product in shelf:
        copy = product.copy()
        copy["actives"] = list(product["actives"])
        data.append(copy)

    with open("data.json", "w") as file:
        json.dump(data, file)
    print("Saved!")


def load_shelf():
    try:
        with open("data.json", "r") as file:
            data = json.load(file)
        loaded = []
        for product in data:
            product["actives"] = set(product["actives"])
            product["open_date"] = tuple(product["open_date"])
            loaded.append(product)
        return loaded
    except FileNotFoundError:
        return []
