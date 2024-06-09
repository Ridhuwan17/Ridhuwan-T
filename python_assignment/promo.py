
promo = {"JIMAT": 15, "BOBATIME" : 20, "HAPPYDAY" : 25, "MYBOBA" : 30}

def printPromo():
    for i, j in zip(promo.keys(), promo.values()):
        print(f"Promo code: {i}, Discount: {j}%")

def applyPromo(user_code,total_price):

    if user_code == 'NO':
        print(f"TOTAL: RM{total_price:.2f}")
        print('Proceed to payment')
        paymentMethod(total_price)
        return total_price

    elif user_code in promo:
        discount = promo[user_code]
        newPrice = total_price - (total_price * (discount / 100))
        print(f"TOTAL: RM{newPrice:.2f}")
        print('Proceed to payment')
        paymentMethod(newPrice)
        return newPrice
    else:
        print("Invalid promo code")
        return applyPromo(user_code,total_price)


def paymentMethod(price):
    print('''Choose a payment method:
            1. Cash
            2. Debit/Credit Card ''')
    payment = int(input('Enter the payment method: '))
    if payment == 1:
        print("Please pay at the counter.")
        print("Order confirmed! Thank you for your order.")

    elif payment == 2:
        card_number = input("Enter your credit card number: ")
        cvv_number = input("Enter your cvv pin: ")
        print("Processing card payment...")
        print("Payment successful!")
        print("Order confirmed! Thank you for your order.")

    else:
        print("Invalid payment method. Please try again.")
        paymentMethod(price)


def promoReceipt(user_code,total):
    if user_code == 'NO':
        print(f"No Promo:\t\t\t\t\t\t\t\t-RM0.00")
        return
    percentage = promo[user_code]
    minus = total*(percentage/100)
    print(f"{user_code}({percentage}% OFF):\t\t\t\t\t\t-RM{minus:.2f}")

