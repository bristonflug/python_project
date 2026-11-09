def show_menu():
    print("\nThe Grill")
    print("1. View inventory")
    print("2. Add or restock an item")
    print("3. Record a sale")
    print("4. Show low-stock alerts")
    print("5. Sales report with charts")
    print("6. Run 30-day simulation")
    print("7. Save and exit")


def view_inventory():
    for item in inventory:
        print("\nItem:", item)
        print("Price: $", inventory[item]["price"])
        print("Quantity:", inventory[item]["qty"])
        print("Reorder level:", inventory[item]["reorder"])


