student={
    "name":"areeba",
    "DOB":25-11-2003,
    "Degree":"BSIT",
}
x=student["name"]
print("Name of a student is: ",x)
x=student.get("DOB")
print("Student birth date: ",x)
x=student.keys()
print("Student dictior is here: ",x)
x=student.values()
print(x)
student["Degree"]="ADP-IT"
print(x)
student["year"]=2025
print(x)
