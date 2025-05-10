# Sort Students by Marks
Student_Marks=[("Areeba",85),("Sidrah",67),("Ali",78),("Zara",90)]
sorted_marks=sorted(Student_Marks,key=lambda x:x[1],reverse=True)
print(sorted_marks)