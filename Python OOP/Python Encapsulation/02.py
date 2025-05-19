# Task:
# Create a class Car with:
# a public attribute brand
# a protected attribute _model
# a private attribute __engine_number
# Add a method show_details() that prints all attributes.
class Car:
    def __init__(self,brand,model,engine_number):
        self.brand=brand
        self._model=model
        self.__engine_number=engine_number
    def show_Details(self):
        print(f"My Car Brand Name: {self.brand}, Model Number: {self._model}, Engine Number: {self.__engine_number}")
c=Car("Suzuki","VXR","SF24")
c.show_Details()