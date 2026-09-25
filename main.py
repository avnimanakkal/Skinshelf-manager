import storage
import product_manager
import expiry
import ingredients
import spending

shelf = storage.load_shelf()


def main():
    while True:
        print("\n===== SKINSHELF =====")
        print("1. Add product")
        print("2. View shelf")
        print("3. Edit product")
        print("4. Delete product")
        print("5. Expiry status")
        print("6. Ingredient check")
        print("7. Spending report")
        print("8. Save and Exit")
        choice = input("Enter choice: ")

        if choice == "1":
            product_manager.add_product(shelf)
        elif choice == "2":
            product_manager.view_shelf(shelf)
        elif choice == "3":
            product_manager.edit_product(shelf)
        elif choice == "4":
            product_manager.delete_product(shelf)
        elif choice == "5":
            expiry.show_expiry_status(shelf)
        elif choice == "6":
            ingredients.check_ingredients(shelf)
        elif choice == "7":
            spending.show_spending_report(shelf)
        elif choice == "8":
            storage.save_shelf(shelf)
            print("Goodbye!")
            break
        else:
            print("Invalid choice, try again.")


main()
