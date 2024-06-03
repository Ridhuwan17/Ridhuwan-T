import userMenu_module
import postLogin_module

dictOfUser = {}

def adminLogin():
    admin_username = "admin"
    admin_password = "admin123"
    
    print("ADMIN LOGIN")
    username = input("Enter admin username: ")
    password = input("Enter admin password: ")
    
    if username == admin_username and password == admin_password:
        print("Admin login successful.")
        postLogin_module.admin_options()
    else:
        print("Invalid admin credentials.")

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
    elif choice == 4:
        adminLogin()

