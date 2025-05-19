# Smart Home Assistant Devices
# Imagine you're building a smart home system where different assistants respond based on their roles. 
#Your base class is SmartDevice, and subclasses will perform device-specific actions.
# SmartLight: Turns on or off lights.
# SmartThermostat: Adjusts temperature.
# SmartSecurityCamera: Notifies user of movement.
class SmartDevice:
    def perform_action(self):
        print("Hello from the cloud I am your smart home device assistant")
class SmartLight(SmartDevice):
    def perform_action(self):
        print("Your order is now my command Your smart light is now on")
class SmartThermostat(SmartDevice):
    def perform_action(self):
        print("Oh It's so hot Wait a sec I figure out your room temperature")
class SmartSecurityCamera(SmartDevice):
    def perform_action(self):
        print("Oh I detect some motion See it immediately Your Smart Cameras are working")
def run_devices(devices):
    devices.perform_action()
smart=[SmartLight(),SmartThermostat(),SmartSecurityCamera()]
for s in smart:
    run_devices(s)
    