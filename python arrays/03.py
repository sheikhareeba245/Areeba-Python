# Create a program to store marks of n students in an array. Allow the user to:
# Enter marks
# Find the highest and lowest marks
# Calculate the average
# Display all marks
n=int(input("Enter number of students: "))
marks=[]
for i in range(n):
    mark=float(input(f"Enter marks for students: {i+1} "))
    marks.append(mark)
print("\n Display marks of all students: ")
for i in range(n):
    print(f"Student {i+1},{marks[i]}")
highest=max(marks)
lowest=min(marks)
average=sum(marks)/n
print("\n Analysis")
print(f"Highest Marks: {highest}")
print(f"Lowest Marks: {lowest}")
print(f"Average Marks: {average:.2f}")