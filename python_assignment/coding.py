import ast

def change_user_detail(username, new_username):
    user_data = []

    with open('userList.txt', 'r') as file:
        lines = file.readlines()

    users = [ast.literal_eval(line.strip()) for line in lines]
    
    if any(user['username'] == new_username for user in users):
        print(f"Username {new_username} already exists.")
        return 

    for user in users:
        if user['username'] == username:
            user['username'] = new_username
            break

    with open('userList.txt', 'w') as file:
        for user in users:
            file.write(str(user) + '\n')

print("""
1. update name
2. update password
3. update age
4. update email
""")

choice = int(input("Enter your choice: "))

if choice == 1:
    new_name = input("Enter your new name: ")
    change_user_detail("pzy", new_name)
elif choice == 2:
    password = input("Enter your newpassword: ")
elif choice == 3:
    age = int(input("Enter your new age: "))
elif choice == 4:
    email = input("Enter your new email: ")
else:
    print("Invalid choice.")
