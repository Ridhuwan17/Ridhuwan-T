import calculate_price
import postLogin_module

promo = {"JIMAT": 15, "BobaTime" : 20, "Happyday" : 25, "MyBoba" : 30}

def applyPromo():
    total = calculate_price.calculate_price()

    for i,j in zip(promo.keys(), promo.values()):
        print(f"Promo code:", i, "Discount:", j, "%" , "  ")

    user_code = input("Enter promo code ('no' to skip): ")
    
    if user_code == 'no':
        print('Returning to the DaBubble Tea Shop page...')#new change
        return postLogin_module.userOption()#new change
    elif user_code in promo:
        discount = promo[user_code]
        newPrice = total - (total*(discount/100))
        print(f"TOTAL: RM{newPrice:.2f}")
        print('Returning to the DaBubble Tea Shop page...')#new change
        return postLogin_module.userOption()#new change
    else:
        print("Invalid promo code,please try again.")
        return applyPromo()