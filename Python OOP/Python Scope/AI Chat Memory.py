# AI Chat Memory Tracker
#  Problem Statement:
# You are designing a simple AI assistant that remembers how many times the user asks about certain topics 
# (like "weather", "news", or "study").
# The assistant should:
# Accept multiple questions from the user.
# Detect the topic using keyword-based AI simulation.
# Update and track the number of times each topic is mentioned using global variables.
# Use local scope inside functions to handle keyword detection.
# Use enclosing scope via a nested function to manage topic count per session.
weather_count=0
news_count=0
study_count=0
def process_questions(user_input):
    global weather_count, news_count, study_count
    def detect_topic():
     lower_input=user_input.lower()
     if "weather" in lower_input:
        return "weather"
     elif "news" in lower_input:
        return "news"
     elif "study" in lower_input:
        return "study"
     else:
        return "unknown"
    topic=detect_topic()
    if topic =="weather":
       weather_count+=1
       print("AI:It's sunny today")
    elif topic =="news":
       news_count+=1
       print("AI:This is your latest headlines")
    elif topic =="study":
       study_count+=1
       print("AI:Stay focused and motivated")
    else:
       print("AI I am not sured how to respond that question")
def show_memory():
   print("\n AI Memory Summary")
   print(f"Weather Question: {weather_count}")
   print(f"News Question: {news_count}")
   print(f"Study Question: {study_count}")
print("Welcome to my  AI Chat Bot")
for i in range(5):
   question=input(f"Enter your question: {i+1} ")
   process_questions(question)
show_memory()
