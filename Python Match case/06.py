# Problem:Input current weather condition:
# "sunny", "rainy", "snowy", "windy", "cloudy"
# Use match-case to suggest an action:
# "sunny" → "Wear sunglasses"
# "rainy" → "Take an umbrella"
# "snowy" → "Wear warm clothes"
# "windy" → "Secure loose items"
# "cloudy" → "Might rain, stay alert"
# Else → "Weather unknown"
weather=input("Enter your weather /sunny,/rainny,/snowy,/windy,/cloudy: ")
match weather:
    case "sunny":
        print("Oh it's sunny outside Please wear your glasses: ")
    case "rainny":
        print("It's rainny outside Make sure you take your umbrella: ")
    case "snowy":
        print("Lot of snow outside your home Wear warm clothes: ")
    case "windy":
        print("Heavey wind breeze outside Secure your loose items: ")
    case "cloudy":
        print("Weather outside is clooudy Might rain Stay alert: ")
    case _:
        print("Unknown weather condition: ")