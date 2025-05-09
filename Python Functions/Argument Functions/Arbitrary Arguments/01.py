#usually we use one or max two arguments use in function but what if we don't know how many arguments we will use so for this problem we use
#Arbitary Arguments short form *args
def greet_friends(*names):
    for name in names:
        print(f"All memebers names are here: {name}")
greet_friends("Areeba", "Jawad","Aiman")
