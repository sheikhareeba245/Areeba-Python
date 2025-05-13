#Modify object properties means you can change the value of attribute of an object after it created
class Teacher():
    def __init__(self,name,age):
        self.name=name
        self.age=age
t=Teacher("Ali",26)
print("Name: ",t.name)
print("Age: ",t.age)
t.age=28
print("Updated age",t.age)