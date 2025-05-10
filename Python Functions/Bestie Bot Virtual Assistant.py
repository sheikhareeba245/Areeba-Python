#Ok now I am creating a beginner level Bestie Bot Virtual Assistant
#Firstly I asked Name and Favourite thing
def bestie_Intro(**kwargs):
    print("Hello g Mohtarma Deakho kiya bnanaya apka liya humna!!")
    for key, value in kwargs.items():
        print(f"{key}: {value}")
def virtual_bestie():
    name=input("Enter your Name: ")
    fav_song=input("Humhain to pata ha apka fav song chalain ap hi bta dain: ")
    fav_food=input("Waisa hain to ap foodie lakin Aj kiya aya apko passand: ")
    hobby=input("Enter your Hobby: ")
    bestie_Intro(Name=name,Song=fav_song,Food=fav_food,Hobby=hobby)
virtual_bestie()
