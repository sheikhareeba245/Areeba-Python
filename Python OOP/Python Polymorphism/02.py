class cat:
    def sound(self):
        print("Meow")
class dog:
    def sound(self):
        print("Bark")
for animals in (cat(),dog()):
    animals.sound()