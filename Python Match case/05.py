# Problem:
# You're building a basic voice assistant.
# Input a command string like:
# "play music"
# "open camera"
# "what's the time"
# "shutdown system"
# Use match-case to print actions or simulated responses.
# Else → "Sorry, I didn't understand that."
command=input("Enter your command you want to give to the voice assistant /play music,/open camera,//what's the time,/shutdown system: ")
match command:
    case "play music":
        print("Ok Sir!I played your favourite music: ")
    case "open camera":
        print("Say Chezz your beautiful face captured by the camera: ")
    case "what's the time":
        from datetime import datetime
        print("Current Time: ",datetime.now().strftime("%H:%M:%S"))
    case "shutdown system":
        print("Your system going to be shutdown!: ")
    case _:
        print("Sorry! I didn't understood your command: ")
 #datetime is a module deals wit dates and time 
 # but inside module there is a class called datetime and we importing module directly in the class
 # datetime.now() gets the current date and time we get year,month,day,hours,minutes,seconds
 # but current we need hours,minutes,seconds
 # strftime this part tells we need time in string format
 # %H means 24 hours
 # %M means minutes
 # %S means seconds
   