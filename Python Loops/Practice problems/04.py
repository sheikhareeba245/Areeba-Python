#4. Daily Temperature Logger
#Take 7 temperature readings (one for each day).
#Skip the reading if user enters a negative number (continue)
#Calculate and print average temperature
#Use for, continue, validation logic
total_temp=0
valid_days=0
for day in range(7):
    temp=float(input(f"Enter temperature for a day {day+1}: "))
    if temp<0:
        print("Invalid reading Skipping.....")
        continue
    total_temp+=temp
    valid_days+=1
if valid_days>0:
    print("Average temperature:",total_temp/valid_days)
else:
    print("No valid temperature data")
    