# Problem:
# Input a string command like "shutdown", "restart", "sleep", or "logout".
# Use match-case to simulate each action (just print the action message).
# If unknown command → "Invalid system command"
command=input("Enter your command like /shutdown,/restart,/sleep,/logout: ").lower()
match command:
    case "shutdown":
        print("Ok computer going to be shutdown: ")
    case "restart":
        print("Ok your computer going to restart: ")
    case "sleep":
        print("Well your laptop is in a sleep condition now: ")
    case "logout":
        print("You must logout your computer before going anywhere: ")
    case _:
        print("Invalid system command: ")
