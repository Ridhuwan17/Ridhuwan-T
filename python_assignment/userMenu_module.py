import postLogin_module
import os
import adminSales
import ast

class Users:
    def __init__(self,username,password,age,email):
        self.username = username
        self.password = password
        self.age = age
        self.email = email

    def loginStatus(self):
        print("Current Session: ",self.username)
    
class Customer(Users):
    def __init__(self, username, password, age, email):
        super().__init__(username, password, age, email)
    
    def customerInfo(self):
        print(f"\nRegistered Info:\n\nUsername: {self.username}\nPassword: {self.password}\nAge: {self.age}\nEmail: {self.email}")

class Admin(Users):
    def __init__(self, username, password):
        super().__init__(username, password, None, None)
        
def welcome():
    print("""
    Welcome to DaBubble Tea Shop
    1. Login
    2. Sign Up
    3. Exit
    """)

def listOfUser_File(dictOfUser):
    with open("userList.txt", "a") as userList:
        formatted_string = f"{dictOfUser}"
        userList.write(formatted_string + "\n")

def userSignUp(dictOfUser):
    print("SIGN UP FORM")
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    age = int(input("Enter your age: "))
    email = input("Enter your email: ")

    new_customer = Customer(username, password, age, email)
    userDetails = {'username': username, 'password': password, 'age': age, 'email': email}

    #creates a new file if it doesnt exist
    if not os.path.exists("userList.txt"):
        with open("userList.txt", "w") as userList:
            pass

    with open("userList.txt", "r") as userList:
        for lines in userList:
            lines = lines.strip()

            if username in lines:
                print("Username already exists. Please try again.")
                return userSignUp(dictOfUser)

    listOfUser_File(userDetails)
    new_customer.customerInfo()
    print(f"\nUser {username} has been successfully registered.")
    print("\nGoing back to the Main Menu")

def userLogin():
    print("LOGIN FORM")
    print("Enter '0' at the username and password to go back to the main menu.\n")

    username_input = input("Enter your username: ")
    password_input = input("Enter your password: ")
    current_user = Users(username_input, password_input, None, None)

    if username_input == '0':
        print("Going back to the main menu...")
        return

    admin_username = "admin"
    admin_password = "admin123"

    if username_input == admin_username and password_input == admin_password:
        print("Admin login successful.")
        current_user.loginStatus()
        adminSales.admin_options()
        return

    with open('userList.txt', 'r') as userList:
        readingLines = userList.readlines()

        if not readingLines:
            print("Invalid username or password or user does not exist. Please try again.\n")
            return userLogin()
        else:
            for line in readingLines:
                user_info = ast.literal_eval(line)
                if user_info['username'] == username_input and user_info['password'] == password_input:
                    current_user.loginStatus()
                    return postLogin_module.userOption(username_input)
                    

            print("Invalid username or password or user does not exist. Please try again.\n")
            return userLogin()



