import promo
import os
from datetime import datetime

order_details = []
order_deets = {}
price = []
order_quantity = []

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

def orderDetails(name,drink_price,order_details,order_deets,price,order_quantity,total_price):
    print(name)
    quantity = int(input('Enter quantity: '))
    order_deets = {"drink": name,"price": drink_price*quantity ,"quantity": quantity}
    order_details.append(order_deets)
    price.append(quantity*drink_price)
    order_quantity.append(quantity)
    total_price += quantity*drink_price

    return order_details,order_deets,price,order_quantity,total_price,quantity

def calculate_price(total_price):
    global order_details,order_deets,price,order_quantity
    while True:
        order = input("Enter your order and type 'done' to finish.(e.g: M to order Mocha): ").upper()
        if order == 'DONE':
            break

        if order == 'A':
            name,drink_price,quantity= "Original Pearl Milk Tea",7,0
            order_details,order_deets,price,order_quantity,total_price,quantity = orderDetails(name,drink_price,order_details,order_deets,price,order_quantity,total_price)
        elif order == "B":
            name,drink_price,quantity= "Signature Brown Sugar Pearl Milk Tea",7,0
            order_details,order_deets,price,order_quantity,total_price,quantity = orderDetails(name,drink_price,order_details,order_deets,price,order_quantity,total_price)
        elif order == "C":
            name,drink_price,quantity= "Classic Roasted Milk Tea with Grass Jelly",7,0
            order_details,order_deets,price,order_quantity,total_price,quantity = orderDetails(name,drink_price,order_details,order_deets,price,order_quantity,total_price)
        elif order == "D":
            name,drink_price,quantity= "Signature Milk Tea",6,0
            order_details,order_deets,price,order_quantity,total_price,quantity = orderDetails(name,drink_price,order_details,order_deets,price,order_quantity,total_price)
        elif order == "E":
            name,drink_price,quantity= "Passionfruit Green Tea",8,0
            order_details,order_deets,price,order_quantity,total_price,quantity= orderDetails(name,drink_price,order_details,order_deets,price,order_quantity,total_price)
        elif order == "F":
            name,drink_price,quantity= "Peach Oolong Tea",8,0
            order_details,order_deets,price,order_quantity,total_price,quantity = orderDetails(name,drink_price,order_details,order_deets,price,order_quantity,total_price)
        elif order == "G":
            name,drink_price,quantity= "Lychee Black Tea",8,0
            order_details,order_deets,price,order_quantity,total_price,quantity = orderDetails(name,drink_price,order_details,order_deets,price,order_quantity,total_price)
        elif order == "H":
            name,drink_price,quantity= "Grapefruit Green Tea",8.5,0
            order_details,order_deets,price,order_quantity,total_price,quantity = orderDetails(name,drink_price,order_details,order_deets,price,order_quantity,total_price)
        elif order == "I":
            name,drink_price,quantity= "Signature Coffee",9,0
            order_details,order_deets,price,order_quantity,total_price,quantity = orderDetails(name,drink_price,order_details,order_deets,price,order_quantity,total_price)
        elif order == "J":
            name,drink_price,quantity= "Hazelnut Latte",10.2,0
            order_details,order_deets,price,order_quantity,total_price,quantity = orderDetails(name,drink_price,order_details,order_deets,price,order_quantity,total_price)
        elif order == "K":
            name,drink_price,quantity= "Americano",10,0
            order_details,order_deets,price,order_quantity,total_price,quantity = orderDetails(name,drink_price,order_details,order_deets,price,order_quantity,total_price)
        elif order == "L":
            name,drink_price,quantity= "Cappucino",10,0
            order_details,order_deets,price,order_quantity,total_price,quantity = orderDetails(name,drink_price,order_details,order_deets,price,order_quantity,total_price)  
        elif order == "M":
            name,drink_price,quantity= "Mocha",11,0
            order_details,order_deets,price,order_quantity,total_price,quantity = orderDetails(name,drink_price,order_details,order_deets,price,order_quantity,total_price)
        else:
            print("Invalid order. Please choose from the menu.")
            continue

    print(f"Your total price is: RM{total_price:.2f}")

    promo.printPromo()
    user_code = input("Enter promo code ('no' to skip): ").upper()
    new_price = promo.applyPromo(user_code,total_price)
    while True:
        amountPaid = float(input('Enter the amount paid: '))
        if amountPaid < new_price:
            print("Insufficient amount paid. Please try again.")
        else:
            break
    balance = amountPaid - new_price
    print_receipt(order_details,price,total_price,new_price,user_code,amountPaid,balance,quantity)

    return {
        "order_details": order_details, 
        "total_price": new_price
    }

def print_receipt(order_details,price,total_price,new_price,user_code,amountPaid,balance,quantity):


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







