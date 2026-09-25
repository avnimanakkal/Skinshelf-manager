clash_rules = [
    ("retinol", "glycolic acid"),
    ("retinol", "salicylic acid"),
    ("retinol", "vitamin c"),
    ("retinol", "benzoyl peroxide")
]


def check_ingredients(shelf):
    print("===== INGREDIENT CHECK =====")
    found_issue = False

    for i in range(len(shelf)):
        for j in range(i + 1, len(shelf)):
            first = shelf[i]
            second = shelf[j]

            shared = first["actives"] & second["actives"]
            if shared:
                print("Overlap:", first["name"], "&", second["name"], "both have", shared)
                found_issue = True

            for a, b in clash_rules:
                if (a in first["actives"] and b in second["actives"]) or \
                   (b in first["actives"] and a in second["actives"]):
                    print("Clash:", first["name"], "&", second["name"], "->", a, "+", b)
                    found_issue = True

    if not found_issue:
        print("No issues found!")
