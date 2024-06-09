
import os
from datetime import datetime

sales_file = "daily_sales.txt"

def admin_options():
    print("""
        1. View Sales for the Day
        2. Reset Sales Counter
        3. Exit Admin Options
    """)
    admin_choice = int(input("Enter your choice(e.g 1): "))
    if admin_choice == 1:
        view_sales()
    elif admin_choice == 2:
       reset_sales()
    elif admin_choice == 3:
        return

def update_sales(amount):
    with open(sales_file, "a") as file:
        date_today = datetime.now().strftime("%d/%m/%Y %I:%M%p")
        file.write(f"{date_today} Total Sales: RM{amount}\n")

def view_sales():
    if not os.path.exists(sales_file):
        print("No sales recorded for today.")
        admin_options()

    with open(sales_file, "r") as file:
        sales = file.readlines()

    total_sales = sum(float(sale.split('RM')[-1]) for sale in sales)
    print(f"Total sales for the day: RM{total_sales:.2f}")
    admin_options()

def reset_sales():
    if os.path.exists(sales_file):
        with open(sales_file, "r") as file:
            previous_sales = file.read()

        with open("previous_sales.txt", "a") as file:
            file.write(previous_sales + "\n")

        os.remove(sales_file)
        print("Sales counter reset and previous sales stored.")
    else:
        print("No sales to reset.")
    admin_options()
