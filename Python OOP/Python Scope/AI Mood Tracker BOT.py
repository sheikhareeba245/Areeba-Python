# AI Mood Tracker Bot
# 🧩 Problem Statement:
# You're building a simple AI-based Mood Tracker Bot that simulates asking a user how they feel throughout the day (e.g., every few hours). 
# The bot analyzes responses using basic keywords (not real NLP) and updates mood statistics.
# You'll use:
# Local scope for processing each mood input.
# Global scope for keeping track of mood stats.
# Enclosing scope to organize internal logic.
happy_count=0
sad_count=0
angry_count=0
stressed_count=0
neutral_count=0
def mood_bot(user_input):
    global happy_count, sad_count, angry_count, stressed_count, neutral_count
    def detect_mood():
        mood=user_input.lower()
        if "happy" in mood or "great" in mood or "good" in mood:
            print("I am glad you are feeling good!!!")
            return "happy"
        elif "sad" in mood or "down" in mood:
            print("Sorry to hear that I hope things get better soon!! ")
            return "sad"
        elif "angry" in mood or "mad" in mood:
            print("It's okay to get angry sometimes Please calam down and take deep breaths!!")
            return "angry"
        elif "stress" in mood or "tierd" in mood:
            print("Please take a break and get some rest!!")
            return "stress"
        else:
            print("Sometimes feeling netural is okay and good!!")
            return "netural"
    mood_result=detect_mood()
    if mood_result =="happy":
        happy_count+=1
    elif mood_result =="sad":
        sad_count+=1
    elif mood_result =="angry":
        angry_count+=1
    elif mood_result =="stress":
        stressed_count+=1
    elif mood_result =="netural":
        neutral_count+=1
def mood_summary():
    print("\n Daily Mood: ")
    print(f"Happy: {happy_count}")
    print(f"Sad: {sad_count}")
    print(f"Angry: {angry_count}")
    print(f"Stress: {stressed_count}")
    print(f"Neutral: {neutral_count}")
print("Welcome to AI Mood Tracker: ")
print("You will be asked 5 times how you are feeling today: ")
for i in range(5):
    mood_input=input(f"Entry {i+1} How are you feeling? ")
    mood_bot(mood_input)
mood_summary()
