master_password = input("What is the master password? ")

def view_passwords():
    with open('passwords.txt', 'r') as f:
        print(f.read())

def add_password():
    site = input("Enter the site/login name: ")
    username = input("Enter the username: ")
    password = input("Enter the password: ")
    with open('passwords.txt', 'a') as f:
        f.write(f"{site} | {username} | {password}\n")

while True:
    mode = input('''
Please enter one of the following modes:
1. view existing passwords
2. add a new password
3. quit
''')

    match mode:
        case "1":
            print("View existing passwords:")
            view_passwords()
        case "2":
            print("Add a new password:")
            add_password()
        case "3":
            print("Goodbye!")
            break
        case _:
            print("Invalid mode")