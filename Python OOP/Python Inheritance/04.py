#__init__ is a constructor method that runs automatically when you create an object
#You use it to initialize values
class Person:
    def __init__(self,name):
        self.name=name
    def show(self):
        print(f"My name is {self.name}")
p=Person("Areeba")
p.show()
#super() methods allow the child class to call method from the parents class especially with__init__
class Person:
    def __init__(self,name):
        self.name=name
class Student(Person):
    def __init__(self, name,grade):
        super().__init__(name)
        self.grade=grade
    def display(self):
        print(f"Name {self.name} Grade {self.grade}")
s=Student("Areeba",'A')
s.display()