# AI Chatbot Roles Using Polymorphism
# You are building a simple AI chatbot system that includes different types of chatbots for specific tasks:
# WeatherBot – Responds with weather updates.
# FinanceBot – Responds with stock market or savings info.
# FitnessBot – Responds with fitness tips.
class ChatBot:
    def respond(self):
        print("Welcome To reebu's ChatBot Where your question's are our first piority")
class WeatherBot(ChatBot):
    def respond(self):
        print("Oh you need update on Weather So here it is latest update of weather conditions in your area")
class FinanceBot(ChatBot):
    def respond(self):
        print("Yes I am also your Financer Here your current finance's")
class FitnessBot(ChatBot):
    def respond(self):
        print("Oh I am glad to know your concerned about your Well-being Here's your this week Fitness Plan")
def interact_with_ChatBot(interact):
    interact.respond()
bot=[WeatherBot(),FinanceBot(),FitnessBot()]
for b in bot:
    interact_with_ChatBot(b)
    