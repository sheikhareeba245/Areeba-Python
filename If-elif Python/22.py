# Problem:
# Input:
# age
# country
# has_id
# Logic:
# If age >= 18 and country is "India":
# If has_id is True: print "Allowed"
# Else: print "ID Required"
age=int(input("Enter your age: "))
country=input("Enter your country: ")
id=input("Enter your id: ")
id=id.lower()=="yes"
if age>=18 and country=="India":
    if id:
     print("Allowed: ")
    else:
     print("ID Required: ")
else:
  print("Not allowed: ")