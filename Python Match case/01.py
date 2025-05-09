#match case use to perform different actions based on different conditions
# Problem:Take a number 1-7 as input.
# Use match-case to print the day name:
# 1 → Monday
# 2 → Tuesday
# ...
# 7 → Sunday
# Else → "Invalid day number"
day=int(input("Enter your number remember number must be between 1 to 7: "))
match day:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case 4:
        print("Thrusday")
    case 5:
        print("Friday")
    case 6:
        print("Saturday")
    case 7:
        print("Sunday")
    case _:
        print("Weekdays are ended: ")