#signup and login system
user={}
def signup():
    print("===Signup===")
    username=input("Create a username: ")
    if username in user:
        print("Username already exists. Try login or choose another method")
    else:
        password=input("Create a password: ")
        user[username]=password
        print(f"Account created succesfully for {username}!")
def login():
    print("===Login===")
    username=input("Enter your username: ")
    password=input("Enter you password: ")
    if username in user and user[username] ==password:
        print(f"Login Successfully Welcome Back {username}")
    elif username in user:
        print("Incorrect password Please Try again: ")
    else:
        print("Username not found Please signup first! ")
def main():
    while True:
        print("\n1. Signup")
        print("2.Login")
        print("3.Exit")
        choice=input("Enter you choice")
        if choice=='1':
            signup()
        elif choice=='2':
            login()
        elif choice=='3':
            print("Thankyou!")
            break
        else:
           print("Invalid Choice: ")
main()
