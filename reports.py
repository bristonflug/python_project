import matplotlib.pyplot as plt

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
