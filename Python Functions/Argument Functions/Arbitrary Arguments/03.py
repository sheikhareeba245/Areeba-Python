#ou’re organizing an event and want to keep track of the people who registered. The function should:
#Accept any number of names
#Display total number of participants
#Print each name in a list
def register_participants(*names):
    print("Number of people are registered: ")
    print(f"Total Participants: {names}")
    for name in names:
        print(f"- {name}")
register_participants("Ali","Sara","Zara","Usman","Hamza","Akram")