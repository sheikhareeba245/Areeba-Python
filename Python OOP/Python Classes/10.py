# Rectangle Area
# Problem Statement:Create a Rectangle class with length and width. 
# Use __init__() to initialize them and create a method area() to return the area of the rectangle.
class Rectangle():
    def __init__(self,lenght,width):
        self.lenght=lenght
        self.width=width
    def area(self):
        return self.lenght*self.width
lenght=float(input("Enter lenght of a rectangle: "))
width=float(input("Enter width of a rectangle: "))
rect=Rectangle(lenght,width)
print(f"\n Area of a rectangle {rect.area()}")
