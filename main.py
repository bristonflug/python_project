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

def load_sales():
    sales = []

    with open("sales.csv", "r", newline="") as file:
        reader = csv.reader(file)
        next(reader)  # Skip the column names.

        for row in reader:
            sale = {
                "date": row[0],
                "item": row[1],
                "qty": int(row[2]),
                "total": float(row[3])
            }
            sales.append(sale)

    return sales


def save_sales(sales):
    with open("sales.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["date", "item", "qty", "total"])

        for sale in sales:
            writer.writerow([
                sale["date"],
                sale["item"],
                sale["qty"],
                sale["total"]
            ])


def valid_date(date):
    parts = date.split("-")
    if len(parts) != 3:
        return False

    year_text = parts[0]
    month_text = parts[1]
    day_text = parts[2]

    if len(year_text) != 4 or len(month_text) != 2 or len(day_text) != 2:
        return False

    if not valid_digits(year_text) or not valid_digits(month_text) or not valid_digits(day_text):
        return False

    year = int(year_text)
    month = int(month_text)
    day = int(day_text)

    if year < 1 or month < 1 or month > 12:
        return False

    days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
        days_in_month[1] = 29

    return day >= 1 and day <= days_in_month[month - 1]


def record_sale(inventory, sales):
    item = input("Item sold: ").strip().lower()
    if item not in inventory:
        print("That item is not in the inventory.")
        return

    qty_text = input("Quantity sold: ").strip()
    if not valid_digits(qty_text):
        print("Enter a positive whole number.")
        return

    quantity = int(qty_text)
    if quantity < 1:
        print("Sell at least one unit.")
        return

    if quantity > inventory[item]["qty"]:
        print("Only", inventory[item]["qty"], "units are in stock.")
        return

    date = input("Sale date (YYYY-MM-DD): ").strip()
    if not valid_date(date):
        print("Enter a valid date like 2026-11-09.")
        return

    total = round(inventory[item]["price"] * quantity, 2)
    sale = {
        "date": date,
        "item": item,
        "qty": quantity,
        "total": total
    }

    inventory[item]["qty"] = inventory[item]["qty"] - quantity
    sales.append(sale)
    print("Sale recorded. Total ($):", total)

inventory = load_inventory()
sales = load_sales()

choice = ""
while choice != "7":
    show_menu()
    choice = input("Choose an option: ").strip()

    if choice == "1":
        view_inventory()
    elif choice == "2":
        add_item()
    elif choice == "3":
        record_sale(inventory, sales)
    elif choice in ["4", "5", "6"]:
        print("Coming soon")
    elif choice == "7":
        save_inventory(inventory)
        save_sales(sales)
        print("Inventory and sales saved. Goodbye!")
    else:
        print("Please choose a number from 1 to 7.")

