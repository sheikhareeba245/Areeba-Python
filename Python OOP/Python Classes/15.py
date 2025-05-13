# Virtual ATM Machine
# Problem Statement:Create a class-based virtual ATM machine simulator.
#  The program should allow the user to:
# Deposit money
# Withdraw money (with a check for insufficient balance)
# Check the current balance
# Use a class to represent the ATM account with attributes and methods for each functionality. 
# This project helps understand encapsulation and method calling in classes.
class ATM:
    def __init__(self,balance=0):
        self.balance=balance
    def deposite(self,amount):
        self.balance+=amount
        print(f"Deposited: {amount}")
    def withdraw(self,amount):
        if amount>self.balance:
            print("Insufficient Balance")
        else:
            self.balance-=amount
            print(f"Withdraw Successfully {amount}")
    def check_balance(self):
        print(f"Current Balance: {self.balance}")
atm=ATM(5000)
user_input=print("Hey Welcome to the ATM!! ")
deposite=float(input("Enter the amount you want to deposite: "))
atm.deposite(deposite)
withdraw=float(input("Enter the amount you want to withdraw: "))
atm.withdraw(withdraw)
atm.check_balance()

