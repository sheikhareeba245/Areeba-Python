# Student Percentage
# Problem Statement:Create a Student class with attributes name, marks1, marks2, marks3. 
# Initialize them in __init__(). 
# Add a method calculate_percentage() that calculates and returns the average percentage of marks.
class Student():
    def __init__(self,name,marks1,marks2,marks3):
        self.name=name
        self.marks1=marks1
        self.marks2=marks2
        self.marks3=marks3
    def calculate_percentage(self):
        total=self.marks1+self.marks2+self.marks3
        percentage=total/3
        return percentage
name=input("Enter your name: ")
marks1=int(input("Enter your marks 1: "))
marks2=int(input("Enter your marks 2: "))
marks3=int(input("Enter your marks 3: "))
s=Student(name,marks1,marks2,marks3)
print(f"My name is {s.name}")
print(f"Marks 1 {s.marks1}")
print(f"Marks 2 {s.marks2}")
print(f"Marks 3 {s.marks3}")
