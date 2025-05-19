# Exercise 2: Global Scope
# Task: Define a global variable count = 0. 
# Create a function increment() that uses the global variable and increases it by 1 using the global keyword.
count=0
def increment():
    global count
    count+=1
    print(f"Inside Function: {count}")
increment()
print(f"Outside Function: {count}")
