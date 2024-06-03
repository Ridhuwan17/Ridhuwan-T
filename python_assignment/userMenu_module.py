import postLogin_module

def welcome():
    print("""
    Welcome to DaBubble Tea Shop
    1. Login
    2. Sign Up
    3. Exit
    4. Admin Login
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

    userDetails = {'username': username, 'password': password, 'age': age, 'email': email}

    with open("userList.txt", "r") as userList:
        for lines in userList:
            lines = lines.strip()
            # lines = lines[2:-3]

            if username in lines:
                print("Username already exists. Please try again.")
                return userSignUp(dictOfUser)

    listOfUser_File(userDetails)

    print(f"\nUser {username} has been successfully registered.")
    print("\nGoing back to the Main Menu")

def userLogin():

    print("LOGIN FORM")
    print("Enter '0' at the username and password to go back to the main menu.\n")

    username = input("Enter your username: ")
    password = input("Enter your password: ")

    if username == '0':
        print("Going back to the main menu...")
        return

    with open('userList.txt','r') as userList:
        readingLines = userList.readlines()

        if not readingLines:
            print("Invalid username or password or user does not exist. Please try again.\n")
            return userLogin()
        else:
            for line in readingLines:
                if username in line and password in line:
                    postLogin_module.userOption() #removed postLogin_module.user_choice(choice=1)
                    return  # Exit the function after successful login
            # If we reach this point, no matching username and password were found
            print("Invalid username or password or user does not exist. Please try again.\n")
            return userLogin()