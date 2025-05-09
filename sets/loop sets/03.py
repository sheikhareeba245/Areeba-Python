# Problem: Find Even Numbers in a Set 
# Question:Write a Python program that loops through a set of numbers and prints only the even numbers.
numbers={22,44,66,45,88,66,12,34,11,33,77}
for num in numbers:
    if num % 2==0:
        print("Numbers are even:",num)
