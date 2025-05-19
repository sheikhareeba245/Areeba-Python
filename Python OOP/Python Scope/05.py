# Exercise 4: Global vs Local Conflict
# Task: Define a global variable x = 10. 
# Then create a function that defines x = 5 inside and prints it. What value of x will be printed inside and outside the function?
x=10
def test():
    x=5
    print("Inner Function: ",x)
test()
print("Outer function: ",x)