#to access the items in the nested dictionary, you the name of the dictionnaries  starting with the outer dictionary
myfamily={
    "Child1":{
        "Name":"Areeba",
        "Age":21
    },
    "Child2":{
        "Name": "AbdulRehman",
        "Age":19
    },
    "Child3":{
        "Name":"Akram",
        "Age":"16"
    }
}
print(myfamily["Child1"]["Name"])
print(myfamily["Child3"]["Age"])
print(myfamily["Child2"]["Name"])
