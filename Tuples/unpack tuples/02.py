#when items in tuple and variables doesn't match we use asterisk* 
fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")
(green,yellow,*red)=fruits
print(green)
print(yellow)
print(red)
