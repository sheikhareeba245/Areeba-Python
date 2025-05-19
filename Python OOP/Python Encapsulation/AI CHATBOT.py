# <!-- You are building a basic AI Chatbot that interacts with users and stores chat history privately.
#  The chatbot should follow the rules of encapsulation to protect user interaction logs.
# Create a class called AIChatBot.
# Add the following attributes:
# name (public) – name of the chatbot.
# __chat_history (private) – a list to store all questions asked by the user.
# Implement these methods:
# ask_question(question):
# Accepts a user question.
# Stores the question in the private list.
# Prints a response like: "BotName: You asked 'question'. I'll answer soon!"
# get_history():
# Displays all past user questions with numbering.
# clear_history():
# Empties the chat history and prints confirmation.
class AIChatBot:
    def __init__(self,name):
        self.name=name
        self.__chat_history=[]
    def ask_questions(self,questions):
        if questions.strip():
            self.__chat_history.append(questions)
            print(f"{self.name} You asked {questions} I will answer soon!!")
        else:
            print("Please ask the valid Question")
    def get_history(self):
        if self.__chat_history:
            print(f"\n Chat History with {self.name}")
            i=1
            for question in self.__chat_history:
                print(str(i)+ " "+question)
                i+=1
        else:
            print("Not chat history yet")
    def clear_history(self):
        self.__chat_history.clear()
        print("Chat History cleared")
bot=AIChatBot("SmartBot")
print("\n Hello I am your SmartBOT")
while True:
    print("\n Choose your Option \n1 Ask Question \n2 View chat History \n3 Clear History \n4 Exit: ")
    choice=input("Enter your choice: ")
    if choice =="1":
        user_input=input("Your question: ")
        bot.ask_questions(user_input)
    elif choice =="2":
        bot.get_history()
    elif choice =="3":
        bot.clear_history()
    elif choice =="4":
        print("Goodbye!!")
    else:
        print("Invalid Choice. Please Try Again")
    