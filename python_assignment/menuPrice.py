import promo
import adminSales
import os
from datetime import datetime

#keeps all the details stored in the order_deets into a list of orders
order_details = []

#stores details of the drink ordered in a dictionary temporarily, e.g drink: .... , price: ...., quantity: ....
order_deets = {}

#stores the price and quantity of the order into a list for receipt purposes
price = []
order_quantity = []

#shows the present timestamp
date_today = datetime.now().strftime("%d/%m/%Y \t\t\t\t\t\t\t\t\t  %I:%M%p")

def menu_boba():
    print("Welcome to Booba T!")
    print("Take a look at our menu and order by typing the desired alphabet!")

    menu_items = {
        "Milk Teas": [
            "(A) Original Pearl Milk Tea \t \t \t \t \t \t RM7.00",
            "(B) Signature Brown Sugar Pearl Milk Tea \t \t \t RM7.00",
            "(C) Classic Roasted Milk Tea with Grass Jelly \t RM7.00",
            "(D) Signature Milk Tea \t \t \t \t \t \t \t RM6.00"
        ],
        "Fruit Teas": [
            "(E) Passionfruit Green Tea \t RM8.00",
            "(F) Peach Oolong Tea \t \t \t RM8.00",
            "(G) Lychee Black Tea \t \t \t RM8.00",
            "(H) Grapefruit Green Tea \t \t RM8.50"
        ],
        "Coffee": [
            "(I) Signature Coffee \t RM9.00",
            "(J) Hazelnut Latte \t RM10.20",
            "(K) Americano \t \t RM10.00",
            "(L) Cappucino \t \t RM10.00",
            "(M) Mocha \t \t \t RM11.00"
        ]
    }

    max_name_length = max(len(item) for items in menu_items.values() for item in items)

    print("~" * (max_name_length + 12))
    print(f"{'Beverage':^{max_name_length + 2}}")
    print("~" * (max_name_length + 12))

    for category, items in menu_items.items():
        print(f"\n{category}:")
        for item in items:
            print(f"- {item:<{max_name_length}}")

    print("~" * (max_name_length + 12))

#after customer finished purchasing, the list will be cleared
def clearPurchaseLog():
    global order_details,price,order_quantity,order_deets
    order_details.clear()
    price.clear()
    order_quantity.clear()
    order_deets.clear()

#prints out the receipt 
def print_receipt(order_details,total_price,new_price,user_code,amountPaid,balance):
    print("-" *65)
    print(f"{'DaBubble Tea Shop':>40}")
    print("-" *65)
    print(f"{'INVOICE':>35}")
    print(f"Date: {date_today}")
    print("-" * 65)
    print(f"{'Order':<45} {'Qty':^7}{'Price(RM)':^8}")
    print("-" *65)
    for order in order_details:
        item = order['drink']
        quantity = order['quantity']
        price = order['price']
        price2 = f'{price:.2f}'
        print(f"{item:<45} {quantity:^7}{price2:^8}")
    print("-" * 65)
    print(f"{'Sub Total':<54}{total_price:.2f}")
    promo.promoReceipt(user_code,total_price)
    print(f"{'Grand Total':<54}{new_price:.2f}")
    print(f"{'Cash':<53} {amountPaid:.2f}")
    print(f"{'Change':<54} {balance:.2f}")

#assigns the appropriate details to the order_deets depending the users' choice of order
def orderDetails(name,drink_price,order_details,order_deets,price,order_quantity,total_price):
    print(name)
    quantity = int(input('Enter quantity: '))
    order_deets = {"drink": name,"price": drink_price*quantity ,"quantity": quantity}
    order_details.append(order_deets)
    price.append(quantity*drink_price)
    order_quantity.append(quantity)
    total_price += quantity*drink_price
    #returns specific data/value needed for other functions
    return order_details,order_deets,price,order_quantity,total_price

#payment section
def paymentSection(order_details,total_price):
    #returns the total price of the order also the promo code if applied
    new_price, user_code = promo.applyPromo(total_price)
    while True:
        #prompts user to enter amount paid
        amountPaid = float(input('\nEnter the amount paid: '))
        if amountPaid < new_price:
            #if amount paid is less than total price, it will prompt user to enter again 
            print("Insufficient amount paid. Please try again.")
        else:
            #stops the 'while' iteration 
            break
    #returns the balance of the user
    balance = amountPaid - new_price
    #prints out the receipt in the terminal
    print_receipt(order_details,total_price,new_price,user_code,amountPaid,balance)
    
    receipt_choice = int(input("\nWould you like a receipt? (1 = Yes, 2 = No): "))
    if receipt_choice == 1:
        if not os.path.exists("receipt.txt"):
            with open("receipt.txt", "w") as receipt:
                pass
        #creates a receipt file for the user
        with open("receipt.txt", "w") as receipt:
            receipt.write("-" *65 + "\n")
            receipt.write(f"{'DaBubble Tea Shop':>40}\n")
            receipt.write("-" *65 + "\n")
            receipt.write(f"{'INVOICE':>35}\n")
            receipt.write(f"Date: {date_today}\n")
            receipt.write("-" * 65 + "\n")
            receipt.write(f"{'Order':<45} {'Qty':^7}{'Price(RM)':^8}\n")
            receipt.write("-" *65 + "\n")
            for order in order_details:
                item = order['drink']
                quantity = order['quantity']
                price = order['price']
                price2 = f'{price:.2f}'
                receipt.write(f"{item:<45} {quantity:^7}{price2:^8}\n")
            receipt.write("-" * 65 + "\n")
            receipt.write(f"{'Sub Total':<54}{total_price:.2f}\n")
            promo.physical_promoReceipt(receipt,user_code,total_price)
            receipt.write(f"{'Grand Total':<54}{new_price:.2f}\n")
            receipt.write(f"{'Cash':<53} {amountPaid:.2f}\n")
            receipt.write(f"{'Change':<54} {balance:.2f}")
        print("\nReceipt has been printed.")
    adminSales.update_sales(new_price)
    print('Thank you for your order!')
    print('Returning to the user page...')

#function to calculate the price of drinks
def calculate_price(total_price):
    #globalize the variables from local function to be used in the main function/anywhere in the program
    global order_details,order_deets,price,order_quantity

    #while loop to keep asking the user to enter their order until they type 'done'
    while True:
        order = input("Enter your order and type 'done' to finish.(e.g: M to order Mocha): ").upper()
        if order == 'DONE':
            print("Returning to user page...\n")
            break
        #choices of drinks
        if order == 'A':
            name,drink_price= "Original Pearl Milk Tea",7
            #stores all data returned data from the orderDetails() function
            order_details,order_deets,price,order_quantity,total_price = orderDetails(name,drink_price,order_details,order_deets,price,order_quantity,total_price)
        elif order == "B":
            name,drink_price= "Signature Brown Sugar Pearl Milk Tea",7
            order_details,order_deets,price,order_quantity,total_price = orderDetails(name,drink_price,order_details,order_deets,price,order_quantity,total_price)
        elif order == "C":
            name,drink_price= "Classic Roasted Milk Tea with Grass Jelly",7
            order_details,order_deets,price,order_quantity,total_price = orderDetails(name,drink_price,order_details,order_deets,price,order_quantity,total_price)
        elif order == "D":
            name,drink_price= "Signature Milk Tea",6
            order_details,order_deets,price,order_quantity,total_price = orderDetails(name,drink_price,order_details,order_deets,price,order_quantity,total_price)
        elif order == "E":
            name,drink_price= "Passionfruit Green Tea",8
            order_details,order_deets,price,order_quantity,total_price= orderDetails(name,drink_price,order_details,order_deets,price,order_quantity,total_price)
        elif order == "F":
            name,drink_price= "Peach Oolong Tea",8
            order_details,order_deets,price,order_quantity,total_price = orderDetails(name,drink_price,order_details,order_deets,price,order_quantity,total_price)
        elif order == "G":
            name,drink_price= "Lychee Black Tea",8
            order_details,order_deets,price,order_quantity,total_price = orderDetails(name,drink_price,order_details,order_deets,price,order_quantity,total_price)
        elif order == "H":
            name,drink_price= "Grapefruit Green Tea",8.5
            order_details,order_deets,price,order_quantity,total_price = orderDetails(name,drink_price,order_details,order_deets,price,order_quantity,total_price)
        elif order == "I":
            name,drink_price= "Signature Coffee",9
            order_details,order_deets,price,order_quantity,total_price = orderDetails(name,drink_price,order_details,order_deets,price,order_quantity,total_price)
        elif order == "J":
            name,drink_price= "Hazelnut Latte",10.2
            order_details,order_deets,price,order_quantity,total_price = orderDetails(name,drink_price,order_details,order_deets,price,order_quantity,total_price)
        elif order == "K":
            name,drink_price= "Americano",10
            order_details,order_deets,price,order_quantity,total_price = orderDetails(name,drink_price,order_details,order_deets,price,order_quantity,total_price)
        elif order == "L":
            name,drink_price= "Cappucino",10
            order_details,order_deets,price,order_quantity,total_price = orderDetails(name,drink_price,order_details,order_deets,price,order_quantity,total_price)  
        elif order == "M":
            name,drink_price= "Mocha",11
            order_details,order_deets,price,order_quantity,total_price = orderDetails(name,drink_price,order_details,order_deets,price,order_quantity,total_price)
        else:
            #if user accidentally or pressed wrong input it will continue to prompt user to keep ordering until 'done'
            print("Invalid order. Please choose from the menu.")
            continue
    #prints out the total price ofthe order
    print(f"Your total price is: RM{total_price:.2f}")

    #returns the order details, total price
    return {
        "order_details": order_details, 
        "total_price": total_price
    }









