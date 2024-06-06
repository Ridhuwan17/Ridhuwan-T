import menu_module
import calculate_price
import salesCounter_module
import admin_module  # Import the admin module
import ast

user_orders = {}
money = 0
totalPricetoPay = 0

def userOption(username):
    print("""
        1. Order Drinks
        2. View Orders
        3. Update User Info
        4. Log Out
    """)
    choice1 = int(input("Enter your choice(e.g 1): "))
    user_choice(username, choice1)

def user_choice(username, choice):
    global totalPricetoPay
    if choice == 1:
        menu_module.menu_boba()
        order = calculate_price.calculate_price(money)
        user_orders[username] = order
        salesCounter_module.update_sales(order['total_price'])
        return userOption(username)
    elif choice == 2:
        print(f"Your order: {user_orders.get(username, 'No orders found')}")
    elif choice == 3:
        update_user_info(username)
    elif choice == 4:
        print("Thank you for coming to the DaBubble Tea Shop")
        exit()

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

    users = [ast.literal_eval(line.strip()) for line in lines]

    if detail == 'username' and any(user['username'] == new_value for user in users):
        print(f"Username {new_value} already exists.")
        return 

    for user in users:
        if user['username'] == username:
            user[detail] = new_value
            break

    with open('userList.txt', 'w') as file:
        for user in users:
            file.write(str(user) + '\n')

