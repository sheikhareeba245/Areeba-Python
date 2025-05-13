# Education System with Inheritance
# Problem:Create a system where there is a Person class and two child classes: Student and Teacher. 
# Every person has a name and age, 
# but a student also has a roll number and marks, and a teacher has a subject.
class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def show_info(self):
        print(f"Name {self.name} Age {self.age}")
class Student(Person):
    def __init__(self, name, age,roll_number,marks):
        super().__init__(name, age)
        self.roll_number=roll_number
        self.marks=marks
    def student_info(self):
        self.show_info()
        print(f"Student roll number {self.roll_number} Marks {self.marks} ")
class Teacher(Person):
        def __init__(self, name, age,subject):
            super().__init__(name, age)
            self.subject=subject
        def teacher_info(self):
            self.show_info()
            print(f"Teacher taught us that subject {self.subject}")
print("Enter student details")
s_name=input("Student name: ")
s_age=int(input("Student age: "))
s_roll=input("Student roll number: ")
s_marks=float(input("Student marks: "))
student=Student(s_name,s_age,s_roll,s_marks)
student.student_info()
print("Enter teacher details")
t_name=input("Teacher name: ")
t_age=input("Teacher age: ")
t_subject=input("Teacher subject: ")
teacher=Teacher(t_name,t_age,t_subject)
teacher.teacher_info()