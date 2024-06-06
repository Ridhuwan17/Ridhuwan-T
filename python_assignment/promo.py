promo = {"JIMAT": 15, "BobaTime": 20, "Happyday": 25, "MyBoba": 30}

def applyPromo(total_price):
    for i, j in zip(promo.keys(), promo.values()):
        print(f"Promo code: {i}, Discount: {j}%")

    user_code = input("Enter promo code ('no' to skip): ")
    
    if user_code == 'no':
        print('Returning to the DaBubble Tea Shop page...')
        return total_price
    
    elif user_code in promo:
        discount = promo[user_code]
        newPrice = total_price - (total_price * (discount / 100))
        print(f"TOTAL: RM{newPrice:.2f}")
        print('\nReturning to the DaBubble Tea Shop page...')
        return newPrice
    else:
        print("Invalid promo code, please try again.")
        return applyPromo(total_price)
