import random

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