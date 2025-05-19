# Task: Implement a voice assistant system that has multiple modes:
# MusicAssistant → prints "Playing your favorite songs..."
# NewsAssistant → prints "Here are today’s top headlines..."
# HealthAssistant → prints "Time to hydrate and take a walk!"
class VoiceAssistant:
    def respond(self):
        print("Hey I am your voiceassistant How can I help you")
class MusicAssistant(VoiceAssistant):
    def respond(self):
        print("Hey I know your favourite song Now I am playing this special for you")
class NewsAssistant(VoiceAssistant):
    def respond(self):
        print("Today's Latest Headlines are here!!")
class HealthAssistant(VoiceAssistant):
    def respond(self):
        print("Oh It's Alert for you Time to hydrate and take a walk for you Promise you feel fresh")
def handle_assistant(assistant):
    assistant.respond()
assist=[MusicAssistant(),NewsAssistant(),HealthAssistant()]
for a in assist:
    handle_assistant(a)