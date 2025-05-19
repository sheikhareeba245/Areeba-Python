# Task:
# Create a class BankAccount with:
# a private attribute __balance
# a method deposit(amount) to add money
# a method withdraw(amount) to subtract money (only if balance is sufficient)
# a method get_balance() to view current balance
class BankAccount:
    def __init__(self):
        self.__balance=0
    def deposite(self,amount):
        if amount>0:
            self.__balance+=amount
            print(f"Amount Deposited Successfully {amount}")
        else:
            print("Deposited amount must be positive")
    def withdraw(self,amount):
        if amount<=self.__balance:
            self.__balance-=amount
            print(f"Amount withdraw successfully {amount}")
        else:
            print("Insufficient amount")
    def get_balance(self):
        return self.__balance
account=BankAccount()
account.deposite(5000)
account.withdraw(4000)
print("Current Balance: ",account.get_balance())
account.withdraw(2000)

