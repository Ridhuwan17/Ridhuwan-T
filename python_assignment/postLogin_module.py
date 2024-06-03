import menu_module
import calculate_price
import salesCounter_module
import ast

# A dictionary to store user orders (for simplicity, store orders in memory)
user_orders = {}

def userOption():
    print("""
        1. Order Drinks
        2. View Orders
        3. Update User Info
        4. Log Out
        5. Admin Options
    """)

def user_choice(username, choice):
    if choice == 1:
        order = calculate_price.calculate_price()
        user_orders[username] = order
        salesCounter_module.update_sales(order['total_price'])
    elif choice == 2:
        print(f"Your order: {user_orders.get(username, 'No orders found')}")
    elif choice == 3:
        update_user_info(username)
    elif choice == 4:
        print("Thank you for coming to the DaBubble Tea Shop")
        exit()
    elif choice == 5:
        admin_options()

def update_user_info(username):
    print("""
    1. Update Name
    2. Update Password
    3. Update Age
    4. Update Email
    """)
    choice = int(input("Enter your choice: "))
    if choice == 1:
        new_name = input("Enter your new name: ")
        change_user_detail(username, 'username', new_name)
    elif choice == 2:
        new_password = input("Enter your new password: ")
        change_user_detail(username, 'password', new_password)
    elif choice == 3:
        new_age = int(input("Enter your new age: "))
        change_user_detail(username, 'age', new_age)
    elif choice == 4:
        new_email = input("Enter your new email: ")
        change_user_detail(username, 'email', new_email)
    else:
        print("Invalid choice")

def change_user_detail(username, detail, new_value):
    user_data = []

    with open('userList.txt', 'r') as file:
        lines = file.readlines()

    # Convert each line to a dictionary
    users = [ast.literal_eval(line.strip()) for line in lines]

    # Check if new_username already exists when updating username
    if detail == 'username' and any(user['username'] == new_value for user in users):
        print(f"Username {new_value} already exists.")
        return 

    # Find the user to update
    for user in users:
        if user['username'] == username:
            user[detail] = new_value
            break

    # Write the updated data back to the file
    with open('userList.txt', 'w') as file:
        for user in users:
            file.write(str(user) + '\n')

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
