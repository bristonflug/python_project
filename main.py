import inventory
import reports

def show_menu():
    print("\nThe Grill - Sales and Inventory Manager")
    print("1. View inventory")
    print("2. Add or restock an item")
    print("3. Record a sale")
    print("4. Show low-stock alerts")
    print("5. Sales report")
    print("6. Run 30-day simulation")
    print("7. Save and exit")
    print("8. Show sales charts")

items = inventory.load_inventory()
sales = inventory.load_sales()

choice = ""

while choice != "7":
    show_menu()
    choice = input("Choose an option: ").strip()

    if choice == "1":
        inventory.view_inventory(items)
    elif choice == "2":
        inventory.add_item(items)
    elif choice == "3":
        inventory.record_sale(items, sales)
    elif choice == "4":
        print("Coming soon")
    elif choice == "5":
        reports.show_report(sales)
    elif choice == "6":
        print("Coming soon")
    elif choice == "7":
        inventory.save_inventory(items)
        inventory.save_sales(sales)
        print("Inventory and sales saved. Goodbye!")
    elif choice == "8":
        reports.show_charts(sales)
    else:
        print("Please choose a number from 1 to 8.")

