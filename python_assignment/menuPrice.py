import promo

order_details = []
price = []
total_price = 0
new_price = 0

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


def calculate_price(total_price):


    while True:
        order = input("Enter your order and type 'done' to finish.(e.g: M to order Mocha): ").upper()
        if order == 'DONE':
            break

        if order == 'A':
            print("Original Pearl Milk Tea")
            order_details.append("Original Pearl Milk Tea")
            price.append(7)
            total_price += 7
        elif order == "B":
            print('Signature Brown Sugar Pearl Milk Tea')
            order_details.append("Signature Brown Sugar Pearl Milk Tea")
            price.append(7)
            total_price += 7
        elif order == "C":
            print('Classic Roasted Milk Tea with Grass Jelly')
            order_details.append("Classic Roasted Milk Tea with Grass Jelly")
            price.append(7)
            total_price += 7
        elif order == "D":
            print('Signature Milk Tea')
            order_details.append("Signature Milk Tea")
            price.append(6)
            total_price += 6
        elif order == "E":
            print('Passionfruit Green Tea')
            order_details.append("Passionfruit Green Tea")
            price.append(8)
            total_price += 8
        elif order == "F":
            print('Peach Oolong Tea')
            order_details.append("Peach Oolong Tea")
            price.append(9)
            total_price += 8
        elif order == "G":
            print('Lychee Black Tea')
            order_details.append("Lychee Black Tea")
            price.append(9)
            total_price += 8
        elif order == "H":
            print('Grapefruit Green Tea')
            order_details.append("Grapefruit Green Tea")
            price.append(8.5)
            total_price += 8.5
        elif order == "I":
            print('Signature Coffee')
            order_details.append("Signature Coffee")
            price.append(9)
            total_price += 9
        elif order == "J":
            print('Hazelnut Latte')
            order_details.append("Hazelnut Latte")
            price.append(10.2)
            total_price += 10.2
        elif order == "K":
            print('Americano')
            order_details.append("Americano")
            price.append(10)
            total_price += 10
        elif order == "L":
            print('Cappuccino')
            order_details.append("Cappuccino")
            price.append(10)
            total_price += 10
        elif order == "M":
            print('Mocha')
            order_details.append("Mocha")
            price.append(11)
            total_price += 11
        else:
            print("Invalid order. Please choose from the menu.")
            continue

    print(f"Your total price is: RM{total_price:.2f}")

    promo.printPromo()
    user_code = input("Enter promo code ('no' to skip): ").upper()
    new_price = promo.applyPromo(user_code,total_price)
    print_receipt(order_details,price,total_price,new_price,user_code)

    return {
        'order_details': order_details,
        'total_price': new_price
    }

def print_receipt(order_details,price,total_price,new_price,user_code):

    print("-" *50)
    print("\t\t\t\t DaBubble Tea Shop ")
    print("-" *50)
    for item, price in zip(order_details,price):
        print(f"{item} \t\t\t\t RM{price:.2f}")
    print("-" * 50)
    print(f"Total: \t\t\t\t\t\t\t\t\t RM{total_price:.2f}")
    promo.promoReceipt(user_code,total_price)
    print("-" *50)
    print(f"Total: \t\t\t\t\t\t\t\t\t RM{new_price:.2f}")
