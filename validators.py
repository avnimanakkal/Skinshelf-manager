def get_number(question):
    while True:
        text = input(question)
        try:
            value = float(text)
            return value
        except ValueError:
            print("That's not a valid number. Please try again.")


def get_whole_number(question, minimum, maximum):
    while True:
        text = input(question)
        try:
            value = int(text)
            if value < minimum or value > maximum:
                print("Please enter a number between", minimum, "and", maximum)
            else:
                return value
        except ValueError:
            print("That's not a valid whole number. Please try again.")


def get_text(question):
    while True:
        value = input(question).strip()
        if value == "":
            print("This can't be empty. Please try again.")
        else:
            return value
