# Animal Sounds
# Problem:Create a Animal class with a method make_sound() that prints "Some generic sound". Then, 
# create two subclasses Dog and Cat that inherit from Animal 
# and override make_sound() to print "Bark" and "Meow" respectively.
class Animal:
    def make_sound(self):
        print("Some generic sound")
class Dog(Animal):
    def make_sound(self):
        print("Bark")
class Cat(Animal):
    def make_sound(self):
        print("Meow")
d=Dog()
c=Cat()
d.make_sound()
c.make_sound()
a=Animal()
a.make_sound()