# Task:
# Create a class Employee with:
# a protected attribute _salary
# a method increase_salary(amount) to increase the salary
# a method show_salary() to view current salary
# Try modifying _salary from outside the class. What do you observe?
class Employee:
    def __init__(self,initial_salary):
        self._salary=initial_salary
    def increase_salary(self,amount):
        if amount>0:
            self._salary+=amount
            print(f"Congratulation Your Salary is increased {amount}")
        else:
            print("Amount must be positive")
    def show_salary(self):
        print(f"Current Salary: {self._salary}")
e=Employee(50000)
e.show_salary()
e.increase_salary(5000)
e.show_salary()
e._salary=10000
e.show_salary()
