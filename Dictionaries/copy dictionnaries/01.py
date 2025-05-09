# we cannot copy dictionay by making this dict1=dict2 because dict2 is the reference of dict1 so any changes made my dict1 will also made in dict2 
# the only method to copy dictionay is the copy()
student={
    "Name":"Ali",
    "Age":21,
    "Blood Group":"O Negative",
    "Favourite Color":"Black",
}
teacher=student.copy()
print(teacher)
print("Dictionary is copied:")