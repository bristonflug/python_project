import csv

def load_inventory():
    inventory = {}

    with open("inventory.csv", "r", newline="") as file:
        reader = csv.reader(file)
        next(reader)

        for row in reader:
            item = row[0]
            inventory[item] = {
                "price": float(row[1]),
                "qty": int(row[2]),
                "reorder": int(row[3])
            }

    return inventory


def save_inventory(inventory):
    with open("inventory.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["item", "price", "qty", "reorder"])

        for item in inventory:
            details = inventory[item]
            writer.writerow([
                item,
                details["price"],
                details["qty"],
                details["reorder"]
            ])


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

def valid_digits(text):
    if text == "" or len(text) > 9:
        return False

    for character in text:
        if character not in "0123456789":
            return False

    return True

def read_quantity(prompt, minimum):
    while True:
        text = input(prompt).strip()

        if valid_digits(text):
            quantity = int(text)
            if quantity >= minimum:
                return quantity

        print("Enter a whole number with up to 9 digits.")
        print("The smallest allowed quantity is", minimum)


def add_item():
    item = input("Item name: ").strip().lower()

    if item == "":
        print("Please enter an item name.")
        return

    if item in inventory:
        quantity = read_quantity("How many units are you adding? ", 1)
        inventory[item]["qty"] = inventory[item]["qty"] + quantity
        print("Updated stock for", item, "is", inventory[item]["qty"])
    else:
        price_text = input("Price, for example 4.50: ").strip()

        while True:
            digits = price_text.replace(".", "", 1)

            if valid_digits(digits):
                price = float(price_text)
                if price > 0:
                    break

            print("Enter a price greater than zero using up to 9 digits.")
            price_text = input("Price: ").strip()

        quantity = read_quantity("Starting quantity: ", 0)
        reorder = read_quantity("Reorder level: ", 0)

        inventory[item] = {
            "price": price,
            "qty": quantity,
            "reorder": reorder
        }

        print("Added", item, "to inventory.")


inventory = load_inventory()

choice = ""

while choice != "7":
    show_menu()
    choice = input("Choose an option: ").strip()

    if choice == "7":
        save_inventory(inventory)
        print("Inventory saved. Goodbye!")
    elif choice == "1":
        view_inventory()
    elif choice == "2":
        add_item()
    elif choice in ["3", "4", "5", "6"]:
        print("Coming soon")
    else:
        print("Please choose a number from 1 to 7.")



