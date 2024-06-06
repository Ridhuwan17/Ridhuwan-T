import salesCounter_module

def admin_options():
    print("""
        1. View Sales for the Day
        2. Reset Sales Counter
        3. Exit Admin Options
    """)
    admin_choice = int(input("Enter your choice(e.g 1): "))
    if admin_choice == 1:
        salesCounter_module.view_sales()
    elif admin_choice == 2:
        salesCounter_module.reset_sales()
    elif admin_choice == 3:
        return
