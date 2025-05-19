# Inheritance Class Polymorphism
#Inheritance allows a child class to inherit properties from their parent class
#Polymorphism allows different characters (inherit from the same parent) to ovveride the same method in their own way
class Employee:
    def show_role(self):
        print("I amm a employee")
class Developer(Employee):
    def show_role(self):
        print("Hey I am a developer I write code")
class Manager(Employee):
    def show_role(self):
        print("I am Manager The actual boss I manage the whole company")
def describe_role(employee):
    employee.show_role()
e1=Developer()
e2=Manager()
describe_role(e1)
describe_role(e2)

