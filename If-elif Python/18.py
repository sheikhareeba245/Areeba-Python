# Problem:Input student marks and print the grade:
# 90+ "A"
# 80-89 "B"
# 70-79  "C"
# 60-69  "D"
# below 60  "F"
marks=int(input("Enter your marks: "))
if marks>90:
    print("Grade A: ")
elif marks>80:
    print("Grade B: ")
elif marks>70:
    print("Grade C: ")
elif marks>60:
    print("Grade D: ")
elif marks<60:
    print("Grade F: ")
else:
    print("Invalid Marks: ")
    