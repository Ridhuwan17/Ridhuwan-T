import os
from datetime import datetime

sales_file = "daily_sales.txt"
previous_sales_file = "previous_sales.txt"
total_profit = 0.0

def update_sales(amount):
    global total_profit
    total_profit += amount
    with open(sales_file, "a") as file:
        date_today = datetime.now().strftime("%d/%m/%Y %I:%M%p")
        file.write(f"{date_today} Total Sales: RM{amount}\n")
    print(f"Current Total Profit: RM{total_profit:.2f}")

def view_sales():
    global total_profit
    if not os.path.exists(sales_file):
        print("No sales recorded for today.")
        return
    
    with open(sales_file, "r") as file:
        sales = file.readlines()
    
    total_sales = sum(float(sale.split('RM')[-1]) for sale in sales)
    print(f"Total sales for the day: RM{total_sales:.2f}")
    print(f"Current Total Profit: RM{total_profit:.2f}")

def reset_sales():
    global total_profit
    if os.path.exists(sales_file):
        with open(sales_file, "r") as file:
            previous_sales = file.read()
        
        with open(previous_sales_file, "a") as file:
            file.write(previous_sales + "\n")
        
        os.remove(sales_file)
        print("Sales counter reset and previous sales stored.")

        # Update the total profit with previous sales
        with open(previous_sales_file, "r") as file:
            previous_sales = file.readlines()
        
        previous_total_sales = sum(float(sale.split('RM')[-1]) for sale in previous_sales)
        total_profit = previous_total_sales

        print(f"Updated Total Profit from previous sales: RM{total_profit:.2f}")
    else:
        print("No sales to reset.")
