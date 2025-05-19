#abstraction means hiding the internalu implementation details and showing only the necessary features to the user
#In OOP Python abstraction use in classes and methods
#For using abstraction Python has buli-in module ABC Abstract Base Class and @abstractmethod this is abstract method
from abc import ABC, abstractmethod
class Vehicle(ABC):
    @abstractmethod
    def start_engine(self):
        pass
class Car(Vehicle):
    def start_engine(self):
        print("Car engine start")
class Bike(Vehicle):
    def start_engine(self):
        print("Bike engine start")
c=Car()
c.start_engine()
b=Bike()
b.start_engine()
#In abstraction we cannot create abstract class objects
