def create_greet(message):
    return lambda name:f"{message},{name}"
greet_hello=create_greet("Hello")
print(greet_hello("Areeba"))
print(greet_hello("Sidrah"))
greet_morning=create_greet("Good Morning")
print(greet_morning("Ali"))
print(greet_morning("Zara"))