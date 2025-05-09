# Problem:
# Input:
# weather (sunny, rainy, cloudy)
# temperature (as int)
# Use match-case:
# If "sunny" and temp > 30 → "Too hot, wear light clothes"
# If "rainy" and temp < 20 → "Cold & wet, carry umbrella & wear warm clothes"
# If "cloudy" and temp between 20–30 → "Mild day, carry a light jacket"
# Else → "No special advice"
weather=input("Enter weather condition /sunny,/rainny,/cloudy: ")
temperature=int(input("Enter temperature: "))
match weather:
    case "sunny":
        if temperature>30:
            print("Too hot, waer lights clothes: ")
        else:
            print("Its Sunny Enjoy the weather: ")
    case "rainny":
        if temperature<=20:
            print("Cold & wet, carry umbrella & wear warm clothes: ")
        else:
            print("It's pleasent weather!: ")
    case "cloudy":
        if 20<=temperature<=30:
            print("Mild day, carry a light jacket: ")
        else:
            print("It's cloudy, dress normally: ")
    case _:
        print("Weather input not recognized: ")