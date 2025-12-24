from cryptography.fernet import Fernet
import os

def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)



def load_key():
    return open("key.key", "rb").read()

master_password = input("What is the master password? ")

if not os.path.exists("key.key"):
    write_key()

key = load_key()
fernet = Fernet(key)

def view_passwords():
    with open('passwords.txt', 'r') as f:
        for line in f.readlines():
            data = line.rstrip()
            site, user, passw = data.split("|")
            print(f"Site: {site}, User: {user}, Password: {str(fernet.decrypt(passw.encode()).decode())}")

def add_password():
    site = input("Enter the site/login name: ")
    username = input("Enter the username: ")
    password = input("Enter the password: ")
    with open('passwords.txt', 'a') as f:
        f.write(f"{site}|{username}|{str(fernet.encrypt(password.encode()).decode())}\n")

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