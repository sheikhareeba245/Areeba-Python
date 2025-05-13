# Student Roll Number Iterator
class Student_Roll_Number:
    def __init__(self,rolls):
        self.rolls=rolls
        self.index=0
    def __iter__(self):
        return self
    def __next__(self):
        if self.index<len(self.rolls):
            roll=self.rolls[self.index]
            self.index+=1
            return roll
        else:
            raise StopIteration
s=Student_Roll_Number([101,102,103,104])
for roll in s:
    print(roll)