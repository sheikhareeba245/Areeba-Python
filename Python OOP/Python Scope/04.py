# Exercise 3: Enclosing Scope
# Task: Create a nested function where the outer function has a variable msg = "Hi", 
# and the inner function prints that variable. Then, modify it using nonlocal.
def outer():
    msg="Hi"
    def inner():
        nonlocal msg
        msg="Hello"
        print("Inner message: ",msg)
    inner()
    print("Outer message: ",msg)
outer()

