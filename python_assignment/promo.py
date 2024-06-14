import menuPrice

#list of promo code
promo = {"JIMAT": 15, "DABOBA" : 20, "HAPPY" : 25, "MYBOBA" : 30}
#initializing the variables
user_code = '0'
total_price = 0

#prints out the available promo code
def printPromo():
    for i, j in zip(promo.keys(), promo.values()):
        print(f"Promo code: {i}, Discount: {j}%")
    print()

#function to apply promo code
def applyPromo(total_price):
    #prints the available promo code
    printPromo()
    #prompts user to enter promo code (upper is used to capitalize all input)
    user_code = input("Enter promo code ('no' to skip): ").upper()

    #if user code is no, then no promo is applied
    if user_code == 'NO':
        print(f"TOTAL: RM{total_price:.2f}")
        print('Proceed to payment')
        print("Order confirmed! Thank you for your order.")
        print("Please pay at the counter.")
        return total_price
    #checks if promo code is valid
    if user_code in promo:
        discount = promo[user_code]
        #calculating the new price of the drinks
        newPrice = total_price - (total_price * (discount / 100))
        print(f"TOTAL: RM{newPrice:.2f}")
        print('\nProceed to payment.....')
        print("\nOrder confirmed! Thank you for your order.")
        print("Please pay at the counter.")
        #ends the loop and the returns the newPrice after promo/no promo code usage
        return newPrice,user_code
    else:
        print("Invalid promo code.Please try again.\n")
        return applyPromo(total_price)

#this function prints out the promo code and its percentage 
def promoReceipt(user_code,total):
    if user_code == 'NO':
        print(f"{'No Promo':<54}{'-0.00'}")
        return
    percentage = promo[user_code]
    minus = total*(percentage/100)
    print(f"{user_code}({percentage}% OFF)\t\t\t\t\t\t\t\t\t\t  -{minus:.2f}")

#function to add new promo code, if the admin wishes to do so
def addPromo():
    newPromo = input("Enter new promo code: ").upper()
    off = int(input("Enter the percentage: "))
    if newPromo not in promo:
        promo.update({newPromo:off})
    else:
        print("Promo Code exists")