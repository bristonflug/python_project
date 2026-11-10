# The Grill — Restaurant Sales & Inventory Manager

## Business Problem
The Grill tracks menu item inventory and sales by hand. This app lets
the manager restock items, record sales, and keep stock counts and
sales records between runs.

## Business Question
At what stock level should we reorder each menu item so we rarely run out?

## How to Run
1. Open the project folder in VS Code.
2. Choose Terminal → New Terminal.
3. Run `py main.py` on Windows, or `python main.py` if that is your Python command.
4. Choose a numbered menu option and follow the prompts.
5. Choose option 7 to save inventory and sales before closing the app.

## Menu Options
1. View inventory — show each item's price, quantity, and reorder level.
2. Add or restock an item — create an item or increase its stock.
3. Record a sale — enter the item, quantity, and date. The app records
   the total and subtracts the units sold from inventory.
4. Show low-stock alerts — coming soon.
5. Sales report with charts — coming soon.
6. Run 30-day simulation — coming soon.
7. Save and exit — save both CSV files and close the program.

## Files
- `main.py` — runs the menu and handles inventory, sales, and CSV files.
- `inventory.csv` — stores each item's name, price, quantity, and reorder level.
- `sales.csv` — stores the date, item, quantity, and total for each sale.

## Author
Briston Flug