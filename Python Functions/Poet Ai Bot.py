#Ok now i am creating A poet Ai Bot according to their mood,name,place
def generate_auto_poem(mood,name,place):
    lines=[
        f"In {place} where silence grew up"
        f"{name} walked with skies so blue"
        f" Through her heart felt a little {mood},",
        f"She smiled, remembering the joy she had"
    ]
    print("\n Here's a poem for you: \n")
    for line in lines:
        print(line)
def generate_custom_poem():
    print("Oh Please genereate your custom 4 lines poem")
    user_line=[]
    for i in range(1,5):
        line=input(f"Line {i}")
        user_line.append(line)
        print("\n Here's your custom poem\n: ")
        for line in user_line:
            print(line)
def ai_poet_bot():
    print("Hi welcome to Ai Poet Bot: Where you read and write your customize poems: ")
    print("1: Let the Bot create a poem: ")
    print("2: Oh you want to create your own poem Well This is Good Best of Luck: ")
    choice=input("Enter your Choice 1 or 2:")
    if choice=="1":
        name=input("Enter you name please! ")
        mood=input("Oh How you are feeling today Please enter this! ")
        place=input("Pick a place e.g(beech,street,room etc): ")
        generate_auto_poem(name,mood,place)
    elif choice=="2":
        generate_custom_poem()
    else:
        print("Invalid Choice Please enter valid choice: ")
ai_poet_bot()
