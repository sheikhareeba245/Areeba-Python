class Student():
    def __init__(self,name):
        self.name=name
    def __str__(self):
        return f"Student Name: {self.name}"
a=Student("Areeba")
print(a)

        