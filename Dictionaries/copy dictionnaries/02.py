# another way to make dictionary copy
student={
    "Name":"Ali",
    "Age":21,
    "Blood Group":"O Negative",
    "Favourite Color":"Black",
}
teacher=dict(student)
print("Dictionary copied: ",teacher)
