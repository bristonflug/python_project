inventory = {
    "burger": {"price": 9.50, "qty": 30, "reorder": 10},
    "fries": {"price": 3.50, "qty": 25, "reorder": 8},
    "chicken sandwich": {"price": 8.50, "qty": 20, "reorder": 6}
}


def view_inventory():
    print("\nCurrent inventory")

    for item in inventory:
        print("Item:", item)
        print("Price: $" + str(inventory[item]["price"]))
        print("Quantity in stock:", inventory[item]["qty"])
        print("Reorder level:", inventory[item]["reorder"])
        print()


def show_menu():
    print("\nThe Grill - Restaurant Sales & Inventory Manager")
    print("1. View inventory")
    print("2. Add or restock an item")
    print("3. Record a sale")
    print("4. Show low-stock alerts")
    print("5. Sales report with charts")
    print("6. Run 30-day simulation")
    print("7. Save and exit")


choice = ""

while choice != "7":
    show_menu()
    choice = input("Choose an option: ").strip()

    if choice == "7":
        print("Goodbye!")
    elif choice == "1":
        view_inventory()
    elif choice in ["2", "3", "4", "5", "6"]:
        print("Coming soon")
    else:
        print("Please choose a number from 1 to 7.")



