#Polumorphism means many forms like it allows classes to treated as if they have the same interface 
# Real-time example
#Think of the word Drive
# A car drives
# A truck drive
# A bike drive
# Even through all of them  a diffrent mechanism but they all share a drive() behavior this is polymorphism
class Teacher:
    def role(self):
        print("I teach students:")
class Student:
    def role(self):
        print("I study and learn")
class Principal:
    def role(self):
        print("I manage the school")
for persons in (Teacher(),Student(),Principal()):
    persons.role()
    
