import userMenu_module
import postLogin_module

dictOfUser = {}

while True:
    userMenu_module.welcome()
    choice = int(input("Enter your choice(e.g 1): "))
    
    if choice == 1:
        userMenu_module.userLogin()
    elif choice == 2:
        userMenu_module.userSignUp(dictOfUser)
    elif choice == 3:
        print("Thank you for coming to the DaBubble Tea Shop")
        exit()
    else:
        print("Invalid choice. Please try again.")
