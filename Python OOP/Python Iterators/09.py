# Countdown Timer (Reverse Order)
class CountDown:
    def __init__(self,start,end):
        self.start=start
        self.end=end
    def __iter__(self):
        return self
    def __next__(self):
        if self.start>=self.end:
            val=self.start
            self.start-=1
            return val
        else:
            raise StopIteration
c=CountDown(5,1)
for i in c:
    print(i)
    