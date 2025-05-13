#Deleting the object properties 
#You can use del keyword to del the specific property of any object
class Teacher():
    def __init__(self,name,age):
        self.name=name
        self.age=age
t=Teacher("Ali",26)
print("Name: ",t.name)
print("Age: ",t.age)
del t.age
print("Name: ",t.name)
print("Age: ",t.age)#see they given us error
#we can alos delete the entire object
del t

