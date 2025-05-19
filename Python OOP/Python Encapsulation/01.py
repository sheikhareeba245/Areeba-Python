#Encapsulation means hiding internal details of how object working and restricting direct access to some of it's parts
#Access Modifiers in Python
#public  name   Accessible everywhere
#private __name Not directly accessible outside the class
#protected _name Meant for internal use only
class Student:
    def __init__(self,name,marks):
        self.name=name #public everyone can access it
        self._roll_no=123 #protected only use internally
        self.__marks=marks
    def show(self):
        print(f"Name: {self.name}, Marks: {self.__marks}, Roll No: {self._roll_no}")
s=Student("Areeba",89)
s.show()