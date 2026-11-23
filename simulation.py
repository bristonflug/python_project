import random
import matplotlib.pyplot as plt

DAYS = 30                   
MIN_DEMAND = 5              
MAX_DEMAND = 20             
STARTING_STOCK = 30         
RESTOCK_AMOUNT = 30         
TRIALS = 1000              
REORDER_LEVELS = [5, 10, 15, 20, 25]  
SHORTAGE_TARGET = 0.5       

def simulate_month(reorder_level):
    stock = STARTING_STOCK
    shortage_days = 0

    for day in range(DAYS):
        if stock <= reorder_level:
            stock = stock + RESTOCK_AMOUNT

        demand = random.randint(MIN_DEMAND, MAX_DEMAND)

        if demand > stock:
            shortage_days = shortage_days + 1
            stock = 0
        else:
            stock = stock - demand

    return shortage_days

def average_shortage_days(reorder_level, trials):
    total_shortage_days = 0

    for trial in range(trials):
        total_shortage_days = total_shortage_days + simulate_month(reorder_level)

    return total_shortage_days / trials


def run_simulation():
    results = []

    print("\n--- Burger Reorder Simulation ---")
    print("Months simulated per reorder level:", TRIALS)
    print("Days per month:", DAYS)
    print("Daily demand:", MIN_DEMAND, "to", MAX_DEMAND)
    print("Restock amount:", RESTOCK_AMOUNT)
    print("Target: fewer than", SHORTAGE_TARGET, "shortage days per month")

    print("\nReorder level    Average shortage days per month")

    for reorder_level in REORDER_LEVELS:
        average = average_shortage_days(reorder_level, TRIALS)
        results.append(average)
        print(reorder_level, "               ", round(average, 3))

    recommended = 0

    for i in range(len(REORDER_LEVELS)):
        if results[i] < SHORTAGE_TARGET and recommended == 0:
            recommended = REORDER_LEVELS[i]

    if recommended == 0:
        print("\nNone of the tested levels met the shortage target.")
        print("Test higher reorder levels or larger deliveries.")
    else:
        print("\nRecommendation: reorder when burger stock reaches",
              recommended, "or fewer.")
        print("This is the lowest tested level that met the shortage target.")
    plt.figure()
    plt.bar(REORDER_LEVELS, results)
    plt.title("The Grill - Burger Reorder Levels")
    plt.xlabel("Reorder level (burgers remaining)")
    plt.ylabel("Average shortage days per 30-day month")
    plt.xticks(REORDER_LEVELS)
    plt.tight_layout()
    plt.savefig("simulation_results.png")
    plt.show()
    plt.close()

    print("Saved simulation_results.png")

