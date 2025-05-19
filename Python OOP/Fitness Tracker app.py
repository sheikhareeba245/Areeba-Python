class user: #Base Class
    def __init__(self,name,age):
        self.name=name
        self.age=age
        self._water_intake=0
        self.__calories_burned=0
    def log_water(self,liters):
        self._water_intake+=liters
        print(f"{liters}L Water added. Total Today: {self._water_intake}L")
    def log_calories(self,calories):
        self.__calories_burned+=calories
    def view_progress(self):
        print(f"\n Name: {self.name}")
        print(f"Water Intake: {self._water_intake}L")
        print(f"Calories Burned: {self.__calories_burned}Kcal")
#Child Class with Polymorphism
class Beginner(user):
    def add_workout(self,activity,duration):
        calories=duration*4
        self.log_calories(calories)
        print(f"{activity} for {duration} mins burned {calories}kcal (Beginner)")
class Intermediate(user):
    def add_workout(self,activity,duration):
        calories=duration*6
        self.log_calories(calories)
        print(f"{activity} for {duration} mins burned {calories}kcal (Intermediate)")
class Advanced(user):
    def add_workout(self,activity,duration):
        calories=duration*8
        self.log_calories(calories)
        print(f"{activity} for {duration} mins burned {calories}kcal (Advanced)")
def create_user():
    name=input("Enter your name: ")
    age=int(input("Enter your age: "))
    level=input("Choose your level (/beginner/intermediate/advanced): ").lower()
    if level =="beginner":
        return Beginner(name,age)
    elif level =="intermediate":
        return Intermediate(name,age)
    elif level =="advanced":
        return Advanced(name,age)
    else:
        print("Invalid Level Defaulting to beginner")
        return Beginner(name,age)
user=create_user()
while True:
    print("\n Menu: \n1 Add Workout: \n2 Log Water Intake: \n3 View Progress: \n4 Exit: ")
    choice=input("Enter your choice (between 1-4): ")
    if choice =="1":
        activity=input("Enter workout activity: ")
        duration=int(input("Enter the duration in minutes: "))
        user.add_workout(activity,duration)
    elif choice =="2":
        liters=float(input("Enter water take in liters: "))
        user.log_water(liters)
    elif choice =="3":
        user.view_progress()
    elif choice =="4":
        print("Session ended exit")
        break
    else:
        print("Invalid choice Please try again")
