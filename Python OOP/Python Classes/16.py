# Smart Home Control Panel
# Problem Statement:Build a simulation of a smart home system where the user can control home appliances
#  like lights, fan, and AC. 
# Use a class to represent the smart home with attributes to track the ON/OFF state of each device. 
class SmartHome:
    def __init__(self):
        self.light=False
        self.Fan=False
        self.AC=False
    def toogle_Light(self):
        self.light=not self.light
        print(f"Light is now {"ON" if self.light else "OFF"}")
    def toogle_Fan(self):
        self.Fan=not self.Fan
        print(f"Fan is now {"ON" if self.Fan else "OFF"}")
    def toogle_AC(self):
        self.AC=not self.AC
        print(f"Ac is now {"ON" if self.AC else "OFF"}")
    def show_status(self):
        print("\n Smart Home Menu")
        print(f"Lights: {"ON"if self.light else "OFF"}")
        print(f"Fan: {"ON" if self.Fan else "OFF"}")
        print(f"AC: {"ON" if self.AC else "OFF"}")
home=SmartHome()
while True:
    print("\nSmart Home Menu")
    print("1: Toogle Lights") 
    print("2: Toogle Fan")
    print("3: Toogle AC") 
    print("4: Show Status") 
    print("5: Exit") 
    choice=input("Enter your choice: ")
    if choice=='1':
        home.toogle_Light()
    elif choice=='2':
        home.toogle_Fan()
    elif choice=='3':
        home.toogle_AC()
    elif choice=='4':
        home.show_status()
    elif choice=='5':
        print("Exiting Smart Home System")
        break
    else:
        print("Invalid Choice Please enter number between 1 to 5: ")