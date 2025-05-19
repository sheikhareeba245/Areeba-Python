# 4. Online Education System
# Abstract class: User
# Child classes: Student, Teacher
# Abstract method: access_portal()
# 🔧 Task: When logged in, students can "view courses", teachers can "upload content". Let the method print these actions differently.
from abc import ABC, abstractmethod
class user(ABC):
    @abstractmethod
    def access_portal(self):
        pass
class Student(user):
    def access_portal(self):
        print("Students access their portal for their assignmenst and results")
class Teacher(user):
    def access_portal(self):
        print("Teacher access the portal and upload lecture and mark attendence")
def login_portal(user_type):
    if user_type.lower()=="Students":
        return Student()
    elif user_type.lower()=="teacher":
        return Teacher()
    else:
        print("Sorry You are not accessed for this portal")
user_input=input("Are you a student or a teacher: ").strip()
user=login_portal(user_input)
if user:
    user.access_portal()
