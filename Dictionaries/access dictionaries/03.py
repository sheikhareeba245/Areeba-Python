#if we want to update the value or add any any item in the dic we use keyword value
student={
    "name":"areeba",
    "DOB":25-11-2003,
    "Degree":"BSIT",
}
x=student.values()
print(x)
student["Degree"]="ADP-IT"
print(x)
student["year"]=2025
print(x)