import menuPrice
import adminSales
import ast

#to store all the users' order
user_orders = {}
#indicates how much money the user has to pay in cart
money = 0

#function for logging in
def userOption(username):
    print("""
        1. Order Drinks
        2. View Orders
        3. Update User Info
        4. Log Out
    """)
    #prompts user to enter thier choice to order,view and etc
    choice1 = int(input("Enter your choice(e.g 1): "))
    #passes the users' choice to the user_choice function 
    user_choice(username, choice1)

#function for user choice
def user_choice(username, choice):
    #order drinks
    if choice == 1:
        #prints the menu of the drinks
        menuPrice.menu_boba()
        #stores all the details of the users' order
        order = menuPrice.calculate_price(money)
        #making sure that the order belongs to the current user
        user_orders[username] = order
        #update the daily sales of DaBubble Tea Shop (networth of the shop)
        adminSales.update_sales(order['total_price'])
        #returns back to the users' page after ordering
        return userOption(username)
    #view orders
    elif choice == 2:
        #checks if the current orders doesnt contain any order
        order = user_orders.get(username, 'No orders found')
        if order == 'No orders found':
            print(order)
        else:
            #if there is an order, print out the order
            print("Your order: {")
            for detail in order['order_details']:
                print("    orders: [{")
                print(f"        drink: {detail['drink']},")
                print(f"        price: {detail['price']},")
                print(f"        quantity: {detail['quantity']}")
                print("    }]")
            print("},",end="")
            print(f"Total price: RM{order['total_price']}")
            
            print('''\n1.Keep Ordering\n2.Pay\n3.Back\n''')
            decision = int(input("Enter your choice:"))

            if decision == 1:
                return userOption(username)
            elif decision == 2:
                menuPrice.paymentSection(order['order_details'], order['total_price'])
                order = []
                menuPrice.clearPurchaseLog()
                return userOption(username)
            elif decision == 3:
                print("Returning to the user's page...")
                return userOption(username)
                
            else:
                print("Invalid choice. Please try again.")
                return userOption(username)
    #update user info
    elif choice == 3:
        #directs the user to the updating users' info page
        update_user_info(username)
        return userOption(username)
    #log out (completely exit the program)
    elif choice == 4:
        print("Thank you for coming to the DaBubble Tea Shop")
        exit()

#update user info function
def update_user_info(username):
    print("""
    1. Update Name
    2. Update Password
    3. Update Age
    4. Update Email

    Enter '0' to go back to the user page
          
    """)
    choice = int(input("Enter your choice: "))

    #go back to the user page if the user wishes to do so
    if choice == 0:
        userOption(username)

    #update name
    if choice == 1:
        new_name = input("Enter your new name: ")
        #function to change name specifically
        change_user_detail(username, 'username', new_name)
        #after updating the name, return to the user page
        return userOption(new_name)
    #update password
    elif choice == 2:
        new_password = input("Enter your new password: ")
        #function to change password specifically
        change_user_detail(username, 'password', new_password)
        #after updating the password, return to the user page
        return userOption(username)
    #update age
    elif choice == 3:
        new_age = int(input("Enter your new age: "))
        #function to change age specifically
        change_user_detail(username, 'age', new_age)
        #after updating the age, return to the user page
        return userOption(username)
    #update email
    elif choice == 4:
        new_email = input("Enter your new email: ")
        #function to change email specifically
        change_user_detail(username, 'email', new_email)
        #after updating the email, return to the user page
        return userOption(username)
    
    else:
        #if the user input is not valid then retry again until complete
        print("Invalid choice. Please try again")
        update_user_info(username)

def change_user_detail(username, detail, new_value):
    #reads the userList.txt file
    with open('userList.txt', 'r') as file:
        lines = file.readlines()

    #parses the lines into a list of dictionaries
    users = [ast.literal_eval(line.strip()) for line in lines]

    #checks if the new username already exists
    if detail == 'username' and any(user['username'] == new_value for user in users):
        print(f"Username {new_value} already exists. Please try again.")
        #goes back to the user update page
        return update_user_info(username)
    #if the new username doesn't exists, then update the details
    for user in users:
        if user['username'] == username:
            user[detail] = new_value
            break
    #overwrite the specific user's details in the userList.txt file
    with open('userList.txt', 'w') as file:
        for user in users:
            file.write(str(user) + '\n')
    
    print(f"\n{detail} updated successfully.\n")
    print('Returning to the DaBubble Tea Page')

