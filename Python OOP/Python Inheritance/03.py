# Superhero Example
# Problem:Make a class Hero with method power() that prints "I have powers!".
# Create a class SpiderMan that inherits from Hero and adds a method web_shoot() that prints "Shooting webs!".
class Hero():
    def power(self):
        print("I have power: ")
class Spiderman(Hero):
    def web_shoot(self):
        print("Shooting Webs!")
s=Spiderman()
s.web_shoot()
s.power()
