# Smart Home Voice Command Tracker
# Problem Statement:You are building a simple AI Smart Home Assistant that responds to voice commands (simulated using input()) 
# and keeps track of how many times certain smart devices are controlled: lights, fan, and AC.
# Your goal:Use local scope inside the command processor.
# Use global scope to track how many times each device was used.
# Use enclosing scope with a nested function to manage device control logic.
# Simulate real-time input using a loop.
lights_count=0
fan_count=0
ac_count=0
def process_command(command):
    global lights_count, fan_count, ac_count
    def closing_device():
        lower_command=command.lower()
        if lower_command =="lights":
            print("Turning ON/OFF Lights")
            return "lights"
        elif lower_command =="fan":
            print("Fan is now running")
            return "fan"
        elif lower_command =="ac":
            print("AC is now ON")
            return "ac"
        else:
            print("Command not recognizeable")
            return "unknown"
    device=closing_device()
    if device =="lights":
        lights_count+=1
    elif device =="ac":
        ac_count+=1
    elif device =="fan":
        fan_count+=1
def show_summary():
    print("\n Smart Home Device usage")
    print(f"Lights used {lights_count} times:")
    print(f"AC used {ac_count} times:")
    print(f"Fan used {fan_count} times:")
print("Welcome to AI Smart Home Assistant")
for i in range(5):
    user_command=input(f"Enter your command {i+1} ")
    process_command(user_command)
show_summary()
    

