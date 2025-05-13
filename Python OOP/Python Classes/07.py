#What if I want that user input their values by itself so what we do for that
class Student():
    def __init__(self,name,age,degree):
        self.name=name
        self.age=age
        self.degree=degree
name=input("Enter your name: ")
age=int(input("Enter your age: "))
degree=input("Enter your degree: ")
s=Student(name,age,degree)
print("\n Enter your personal info please! ")
print("Name",s.name)
print("Age",s.age)
print(f"Degree {s.degree}")
