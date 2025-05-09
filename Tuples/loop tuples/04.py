# Problem: Count Occurrences of an Item in a Tuple
# Question:Write a Python program to count the occurrences of a specific item in a tuple.
# The program should take a tuple and a value as input.
# It should return how many times the value appears in the tuple.
numbers=[1,2,3,4,5,6,7,8,9]
target=2
count=numbers.count(target)
print(f"{target} appears {count} times in the tuple: ")
