import csv
import matplotlib.pyplot as plt

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

def group_units_by_item(sales):
    totals = {}

    for sale in sales:
        item = sale["item"]

        if item not in totals:
            totals[item] = 0

        totals[item] = totals[item] + sale["qty"]

    return totals


def show_report(sales):
    if len(sales) == 0:
        print("No sales recorded yet.")
        return

    total_units = 0
    total_revenue = 0

    for sale in sales:
        total_units = total_units + sale["qty"]
        total_revenue = total_revenue + sale["total"]

    average_sale = total_revenue / len(sales)
    units_by_item = group_units_by_item(sales)

    highest_units = 0

    for item in units_by_item:
        if units_by_item[item] > highest_units:
            highest_units = units_by_item[item]

    print("\n--- Sales Report ---")
    print("Sales recorded:", len(sales))
    print("Total units sold:", total_units)
    print("Total revenue ($):", round(total_revenue, 2))
    print("Average sale amount ($):", round(average_sale, 2))

    print("\nBest-selling item(s):")

    for item in units_by_item:
        if units_by_item[item] == highest_units:
            print(item, "-", highest_units, "units")

    print("\nUnits sold by item:")

    for item in units_by_item:
        print(item, "-", units_by_item[item], "units")


def group_units_by_day(sales):
    totals = {}

    for sale in sales:
        date = sale["date"]

        if date not in totals:
            totals[date] = 0

        totals[date] = totals[date] + sale["qty"]

    return totals


def show_charts(sales):
    if len(sales) == 0:
        print("No sales recorded yet. Record a sale first.")
        return

    units_by_item = group_units_by_item(sales)
    items = []
    item_units = []

    for item in units_by_item:
        items.append(item)
        item_units.append(units_by_item[item])

    plt.figure()
    plt.bar(items, item_units)
    plt.title("The Grill - Units Sold by Item")
    plt.xlabel("Menu item")
    plt.ylabel("Units sold")
    plt.xticks(rotation=30)
    plt.tight_layout()
    plt.savefig("units_by_item.png")
    plt.show()
    plt.close()

    units_by_day = group_units_by_day(sales)
    dates = []

    for date in units_by_day:
        dates.append(date)

    dates.sort()
    daily_units = []

    for date in dates:
        daily_units.append(units_by_day[date])

    plt.figure()
    plt.plot(dates, daily_units, marker="o")
    plt.title("The Grill - Units Sold by Day")
    plt.xlabel("Date")
    plt.ylabel("Units sold")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig("units_by_day.png")
    plt.show()
    plt.close()

    print("Saved units_by_item.png and units_by_day.png")


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
    elif choice == "4":
        print("Coming soon")
    elif choice == "5":
        show_report(sales)
    elif choice == "6":
        print("Coming soon")
    elif choice == "7":
        save_inventory(inventory)
        save_sales(sales)
        print("Inventory and sales saved. Goodbye!")
    elif choice == "8":
        show_charts(sales)
    else:
        print("Please choose a number from 1 to 8.")

