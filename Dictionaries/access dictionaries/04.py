#the item keyword return value in form of tuples and is key: value pairs
student={
    "name":"areeba",
    "DOB":25-11-2003,
    "Degree":"BSIT",
}
x=student.items()
print(x)
#we also upddate the using this
student={
    "name":"areeba",
    "DOB":25-11-2003,
    "Degree":"BSIT",
}
student["Degree"]="ADP-IT"
student["Graduation year"]=2024
student.items()
