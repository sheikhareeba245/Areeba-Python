#Inheritance is the OOP Features that allows a class(child) to inherit properties and methods from another class(parent)
class Parent:
    def show(self):
        print("This is parent class: ")
class child(Parent):
    def display(self):
        print(("This is the child class: "))
c=child()
c.show()
c.display()
p=Parent()
p.show()