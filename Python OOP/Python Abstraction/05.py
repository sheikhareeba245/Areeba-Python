# AI Voice Command System
# Abstract class: VoiceCommand
# Child classes: PlayMusic, TellWeather, SetReminder
# Abstract method: execute(command)
from abc import ABC, abstractmethod
class VoiceCommand(ABC):
    @abstractmethod
    def execute(self,command):
        pass
class Playmusic(VoiceCommand):
    def execute(self, command):
        print(f"Play your favourite music sound {command}")
class TellWeather(VoiceCommand):
    def execute(self, command):
        print(f"Today's weather in {command} is: Sunny with light winds")
class SetReminder(VoiceCommand):
    def execute(self, command):
        print(f"Reminder set for: {command}")
def process_command(action,data):
    if action=="music":
        return Playmusic()
    elif action=="weather":
        return TellWeather()
    elif action=="reminder":
        return SetReminder()
    else:
        print("Invalid command")
        return None
action_input=input("What do you want? (music/weather/Reminder)").strip() .lower()
data_input=input("Enter the detail you want: (music name/city name/reminder)").strip()
cmd=process_command(action_input,data_input)
if cmd:
    cmd.execute(data_input)
