#__init()__ constructor method is a special method in python class It automatically runs when you create object
#It helps you to assgns values to the object properties at that time of creation
class Student():
    def __init__(self,name,age,degree):
        self.name=name
        self.age=age
        self.degree=degree
s=Student("Areeba",21,"IT")
print(s.name)
print(s.age)
print(s.degree)
s1=Student("Ali",24,"CS")
s2=Student("Zara",19,"ICS")
s3=Student("Fatima",20,"Medical")
print(s2.name)
print(s3.degree)
print(s1.age)
#Question is that what is the diffrence between above code and follow code
class Student:
    name="Areeba"
    age=21
    degree="IT"
a=Student()
print(a.name)
print(a.age)
print(a.degree)
#So answer is that in without __init_  program values like name,age and degree is fixed for every object
#like jo bhi object bna gha to uska name areeba,age 21,and degree IT hi ho ghi 
#Customization possible nhi ho ghi
#and With __init__ wala method ma jb bhi object create ho gha usko values kud da sakti hoon
#hr object ka liya alag values hoon ghi just like above code 
# I take four different objects and assign different value

