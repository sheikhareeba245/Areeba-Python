# Multiples of a Number
class Multiples:
    def __init__(self,number,count):
        self.number=number
        self.count=count
        self.current=1
    def __iter__(self):
        return self
    def __next__(self):
        if self.current<=self.count:
         result=self.number*self.current
         self.current+=1
         return result
        else: 
           raise StopIteration
m=Multiples(3,10)
for i in m:
   print(i)