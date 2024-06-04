import promo

def calculate_price(total_price):
    # total_price = 0.0  # Initialize total price
    order_details = []

    # Get user's order
    while True:
        order = input("Enter your order and type 'done' to finish.(e.g: M to order Mocha): ").upper()
        if order == 'DONE':
            break

        if order == 'A':
            print("Original Pearl Milk Tea")
            order_details.append("Original Pearl Milk Tea")
            total_price += 7

        elif order == "B":
            print('Signature Brown Sugar Pearl Milk Tea')
            order_details.append("Signature Brown Sugar Pearl Milk Tea")
            total_price += 7

        elif order == "C":
            print('Classic Roasted Milk Tea with Grass Jelly')
            order_details.append("Classic Roasted Milk Tea with Grass Jelly")
            total_price += 7

        elif order == "D":
            print('Signature Milk Tea')
            order_details.append("Signature Milk Tea")
            total_price += 6

        elif order == "E":
            print('Passionfruit Green Tea')
            order_details.append("Passionfruit Green Tea")
            total_price += 8

        elif order == "F":
            print('Peach Oolong Tea')
            order_details.append("Peach Oolong Tea")
            total_price += 8

        elif order == "G":
            print('Lychee Black Tea')
            order_details.append("Lychee Black Tea")
            total_price += 8

        elif order == "H":
            print('Grapefruit Green Tea')
            order_details.append("Grapefruit Green Tea")
            total_price += 8.5

        elif order == "I":
            print('Signature Coffee')
            order_details.append("Signature Coffee")
            total_price += 9

        elif order == "J":
            print('Hazelnut Latte')
            order_details.append("Hazelnut Latte")
            total_price += 10.2

        elif order == "K":
            print('Americano')
            order_details.append("Americano")
            total_price += 10

        elif order == "L":
            print('Cappuccino')
            order_details.append("Cappuccino")
            total_price += 10

        elif order == "M":
            print('Mocha')
            order_details.append("Mocha")
            total_price += 11

        else:
            print("Invalid order. Please choose from the menu.")
            continue

    # Print the total price
    print(f"Your total price is: RM{total_price:.2f}")  # Format price with 2 decimal places

    promoCodeList = promo.promo

    total_price = promo.applyPromo(total_price)

    return {
        'order_details': order_details,
        'total_price': total_price
    }
