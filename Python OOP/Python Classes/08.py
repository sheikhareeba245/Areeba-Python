# Bank Account
# Problem Statement:Create a BankAccount class with attributes name and balance. Initialize these with __init__(). 
# Also create a method display_balance() to show the user’s name and balance.
class Bank_Account():
    def __init__(self,user,balance):
        self.user=user
        self.balance=balance
user=input("Enter your user name: ")
balance=float(input("Enter your current balance: "))
b=Bank_Account(user,balance)
print(f"User Name {b.user}")
print(f"Current Balance {b.balance}")
