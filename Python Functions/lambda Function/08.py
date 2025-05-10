# Create a function power_function(power) that returns a lambda function. This lambda should take a number and raise it to the given power.
def power_function(power):
    return lambda num: num**power
square=power_function(2)
print(square(5))
cube=power_function(3)
print(cube(9))
