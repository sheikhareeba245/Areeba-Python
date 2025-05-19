#Python Scope define where your variable can be accessed or used inside the code
#Types of Scope in Python LEGB Rule
#L-Local:Names inside a function or method
#E-Enclosing:Names in the outer function
#G-Global:Names defined at the top-level
#B-Built-in: Names that are defined by Python(len(),print() etc)
#Local Scope:declared inside a function
def my_function():
    x=10 #declared local scope
    print(x)
my_function()
#Global Scope: declared outside all function is global and can be used inside function using global keyword
x=50 #global variable
def my_function():
    global x
    print(x) #accessing global variable inside the function
my_function()
print(x) #also accessed outside the function
#Changing global variable inside the function
count=0
def increment():
    global count
    count+=1
    print("Inside Function: ",count)
increment()
print("Outside the function: ",count)
#Enclosing scope : used in nested function The inner function accesed the variable of the outer function but cannot modify
def outer():
    msg="Hello"
    def inner():
        print(msg) #Access enclosing variable
    inner()
outer()
#If I want to modify enclosing scope so we used nonlocal
def outer():
    msg="hello"
    def inner():
        nonlocal msg
        msg="Hi"
        print("Inner: ",msg)
    inner()
    print("Outer: ",msg)
outer()
#Built-in scope: Python has some built-in function
print(len("Areeba"))

