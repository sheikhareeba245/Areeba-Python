# AI ChatBot Inheritance 
# Problem Statement:You're creating a basic chatbot system. 
# You have a base class ChatBot that stores the name of the bot and a general respond() method.
# You create two specific bots by inheriting from ChatBot:
# MotivationBot (gives motivational responses)
# StudyBot (gives study tips)
# Each child class overrides the respond() method.
class ChatBOT:
    def __init__(self,name):
        self.name=name
    def respond(self):
        print(f"{self.name} Hello I am here to help you!! ")
class MotivationBot(ChatBOT):
        def respond(self):
         print(f"{self.name} Keep going Your are doing great job")
class StudyBot(ChatBOT):
         def respond(self):
          print(f"{self.name} Remember take breaks and foucused on your study")
bot_type=input("Which type of BOT you required: ")
if bot_type =="motivation":
   bot=MotivationBot("Motivo")
elif bot_type =="study":
   bot=StudyBot("StudyMate")
else:
   bot=ChatBOT("GerneralBOT")
bot.respond()

